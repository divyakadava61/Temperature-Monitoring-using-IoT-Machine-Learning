# Temperature-Monitoring-using-IoT-Machine-Learning
# Description
This project is a real-world Industrial IoT application that uses a Bolt WiFi module and LM35 temperature sensor to monitor, predict, and alert temperature anomalies during the pharmaceutical manufacturing process, specifically in tablet production. It combines IoT hardware with Machine Learning (Polynomial Regression and Z-score Analysis) to ensure compliance with regulatory temperature constraints and optimize process reliability.
# Goal
Develop an IoT-based temperature monitoring system to:
- Predict potential temperature violations using polynomial regression.
- Detect anomalies such as fridge/chamber door openings without additional hardware.
- Trigger real-time email alerts when temperature thresholds are breached.
- Ensure adherence to government-imposed pharma manufacturing conditions.
# Process
1. Hardware Setup
   - Sensor: LM35 temperature sensor connected to the Bolt IoT WiFi module.
   - Environment: Simulated using a household refrigerator (as industrial cooling chambers were unavailable).
   - Power: 5V DC adapter.
  
     ![image](https://github.com/user-attachments/assets/4a1ffed3-1560-4999-b05c-6fb0f0903320)

2. Data Acquisition & Cloud Integration
   - Connected LM35 to the Bolt module using female-to-male jumper wires.
   - Configured Bolt Cloud to read analog values from the sensor every 5 minutes.
   - Stored and visualized data using the Bolt Cloud dashboard. 
3. Predictive Monitoring with Polynomial Regression
   Wrote a JavaScript code to:
   - Collect real-time sensor data.
   - Run polynomial regression on the temperature trend.
   - Predict if the temperature would stay between -33°C and -30°C for more than 20 minutes.
4. Anomaly Detection via Z-score Analysis
   - Implemented Z-score anomaly detection to monitor sudden changes in sensor readings.
   - Tuned the model to detect spikes when the fridge door is opened (simulating human intervention).
   - No extra sensors were used to detect door state—purely based on temperature fluctuation.
5. Email Alerts using Mailgun API
   Configured a Python script to send real-time email alerts when:
   - The temperature crossed safe thresholds.
   - A possible door opening was detected via Z-score analysis.
# Insights
- Data-driven alerts reduced the need for constant manual monitoring.
- Z-score analysis successfully detected door openings with no need for contact sensors.
- Polynomial regression enabled forecasting and timely intervention before conditions became non-compliant.
- Demonstrated how low-cost hardware and simple ML models can enforce safety standards in sensitive industrial processes.
  
  ![image](https://github.com/user-attachments/assets/284b8c70-6964-456c-bfe1-3f04a7871f35)

# Conclusion
This project illustrates the synergy between IoT and Machine Learning in building smart, responsive, and regulation-compliant systems. It is an efficient solution for pharmaceutical manufacturing, where temperature control is critical. The use of Bolt IoT, LM35, cloud integration, and Python-based predictive modeling makes the system reliable and scalable with minimal hardware.
