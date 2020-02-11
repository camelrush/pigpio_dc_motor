import pigpio
import time

MOTOR_OUT1_PIN = 23
MOTOR_OUT2_PIN = 24
MOTOR_OPWM_PIN = 18
FREQ = 100
RANGE = 255

pig = pigpio.pi()

pig.set_mode(MOTOR_OUT1_PIN, pigpio.OUTPUT)
pig.set_mode(MOTOR_OUT2_PIN, pigpio.OUTPUT)
pig.set_mode(MOTOR_OPWM_PIN, pigpio.OUTPUT)

# 正転 low
print("正転(low)")
pig.write(MOTOR_OUT1_PIN ,1)
pig.write(MOTOR_OUT2_PIN ,0)
pig.set_PWM_dutycycle(MOTOR_OPWM_PIN, 10)
time.sleep(2.0)

# 正転 high
print("正転(high)")
pig.write(MOTOR_OUT1_PIN ,1)
pig.write(MOTOR_OUT2_PIN ,0)
pig.set_PWM_dutycycle(MOTOR_OPWM_PIN, 255)
time.sleep(2.0)

# ブレーキ
print("ブレーキ")
pig.write(MOTOR_OUT1_PIN ,1)
pig.write(MOTOR_OUT2_PIN ,1)
pig.set_PWM_dutycycle(MOTOR_OPWM_PIN, 100)
time.sleep(2.0)

# 逆転
print("逆転")
pig.write(MOTOR_OUT1_PIN ,0)
pig.write(MOTOR_OUT2_PIN ,1)
pig.set_PWM_dutycycle(MOTOR_OPWM_PIN, 100)
time.sleep(2.0)

# 停止
print("停止")
pig.write(MOTOR_OUT1_PIN ,0)
pig.write(MOTOR_OUT2_PIN ,0)
time.sleep(2.0)

pig.set_PWM_dutycycle(MOTOR_OPWM_PIN, 0)
pig.stop()
