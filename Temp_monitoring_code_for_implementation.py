import smtplib
import email_conf,json,time
from boltiot import Email,Bolt
import math, statistics


minimum_limit = 50 #the minimum threshold of temp value
maximum_limit = 90 #the maximum threshold of temp value

mybolt = Bolt(email_conf.API_KEY, email_conf.DEVICE_ID)
mailer = Email(email_conf.MAILGUN_API_KEY, email_conf.SANDBOX_URL, email_conf.SENDER_EMAIL, email_conf.RECIPIENT_EMAIL)

def compute_bounds(history_data,frame_size,factor):
    if len(history_data)<frame_size :
        return None

    if len(history_data)>frame_size :
        del history_data[0:len(history_data)-frame_size]
    Mn=statistics.mean(history_data)
    Variance=0
    for data in history_data :
        Variance += math.pow((data-Mn),2)
    Zn = factor * math.sqrt(Variance / frame_size)
    High_bound = history_data[frame_size-1]+Zn
    Low_bound = history_data[frame_size-1]-Zn
    return [High_bound,Low_bound]

history_data=[]



while True:
        print("Reading The Sensor Value: ")
        response = mybolt.analogRead('A0')
        data = json.loads(response)
        print ("Sensor value is: " + str(data['value']))
        try:
                sensor_value = int(data['value'])
#Anomaly Detection
                bound = compute_bounds(history_data,email_conf.FRAME_SIZE,email_conf.MUL_FACTOR)
                if not bound:
                        required_data_count=email_conf.FRAME_SIZE-len(history_data)
                        print("Not enough data to compute Z-score. Need ",required_data_count," more data points")
                        history_data.append(int(data['value']))
                        time.sleep(10)
                        continue

                try:
                        if sensor_value > bound[0] :
                                print("bound[0] = ",bound[0])
                                print ("Someone has opened the fridge door")
                                print("This is the response ",response)
                        elif sensor_value < bound[1]:
                                print("bound[1] = ",bound[1])
                                print ("Someone has opened the fridge door")
                                print("This is the response ",response)
                        history_data.append(sensor_value);
                        time.sleep(10)

                except Exception as e:
                        print ("Error",e)
                        continue

                #Email send if temprature crossed threshold
                if sensor_value > maximum_limit or sensor_value < minimum_limit:
                        print ("Tempurature Crosses Threshold")
                        print(sensor_value)
                        response = mailer.send_email("Alert", "The current temperature sensor value is " +str(sensor_value))
                        response_text = json.loads(response.text)
print("Response recieved from Mailgun: " + str(response_text['message']))
        except Exception as e:
                print ("Error occured: Below are the details")
                print (e)
                time.sleep(10)
