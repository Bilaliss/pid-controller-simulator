import time
import matplotlib.pyplot as plt

class PID:
    def __init__(self, Kp, Ki, Kd, setpoint):
        self.Kp = Kp
        self.Ki = Ki
        self.Kd = Kd
        self.setpoint = setpoint
        self.prev_error = 0
        self.integral = 0

    def update(self, current_value, dt):
        error = self.setpoint - current_value
        self.integral += error * dt
        derivative = (error - self.prev_error) / dt
        output = self.Kp * error + self.Ki * self.integral + self.Kd * derivative
        self.prev_error = error
        return output

# Simulazione
setpoint = 50.0
current_value = 20.0
pid = PID(Kp=0.6, Ki=0.1, Kd=0.05, setpoint=setpoint)

values = []
time_values = []
dt = 0.1

for i in range(200):
    control = pid.update(current_value, dt)
    current_value += control * dt  # sistema semplificato
    values.append(current_value)
    time_values.append(i * dt)
    time.sleep(0.01)

plt.plot(time_values, values)
plt.axhline(y=setpoint, color='r', linestyle='--', label='Setpoint')
plt.xlabel('Tempo (s)')
plt.ylabel('Valore')
plt.title('Simulazione PID Controller')
plt.legend()
plt.grid()
plt.show()
