# from ax12 import Ax12
import time
from util.observer import Observable


class MovementControls(Observable):
    """Manages movement controls"""

    def __init__(self, num_legs=6, leg_joints=3):
        """Init"""
        super().__init__()
        print("class: MovementControls created.")
        self.legs = [self.Leg(i, leg_joints) for i in range(num_legs)]

    def notifyObservers(self, arg=None):
        """Notifies the observers"""
        self.setChanged()
        Observable.notifyObservers(self, arg)

    def command(self):
        self.print_legs()
        self.walk(100)

    def print_legs(self):
        # test
        print("test: function print_legs executed..")
        print([l.servos for l in self.legs])

    def walk(self, num_steps):
        # test
        print("test: function walk executed..")
        for l in self.legs:
            l.reset()

        l = self.legs[5]
        for _ in range(num_steps):
            l.raise_leg()
            time.sleep(1)
            l.step()
            time.sleep(1)

        for _ in range(num_steps):
            for l in self.legs:
                if l.direction == 0:
                    continue
                l.raise_leg()
            time.sleep(1)
            for l in self.legs:
                l.step()
            time.sleep(3)

            for i in range(13):
                print("uncomment next line")
                # Ax12().readPosition(i + 1))

        for _ in range(num_steps):
            for l in self.legs:
                l.raise_leg()
                time.sleep(0.002)
            time.sleep(2)
            for l in self.legs:
                l.step()
                time.sleep(0.002)
            # time.sleep(0.5)

    class Leg:
        """Controls a leg"""

        def __init__(self, leg_num, num_servos):
            """Init"""
            print("sub-class: Leg created.")
            self.servos = [leg_num * num_servos + i + 1 for i in range(3)]
            self.direction = leg_num % 2
            self.num_legs = leg_num

        @staticmethod
        def move_servo(servo_idx, angle, speed):
            """Moves a servo"""
            # test
            print("test: function move_servo executed..")
            try:
                print("uncomment next line")
                # Ax12().moveSpeed(servo_idx, angle, speed)
            except IndexError:
                print(servo_idx + " Out of range")
                return
            except:
                print("\nCould not move Servo " + str(servo_idx))
                # traceback.print_exc(file=sys.stdout)

        def raise_leg(self):
            """Raises a leg"""
            # test
            print("test: function raise_leg executed..")
            speed = 200
            sleep_time = 0.01
            if self.direction == 1:
                self.move_servo(self.servos[1], 150, speed)
                time.sleep(sleep_time)
                self.move_servo(self.servos[2], 150, speed)
                time.sleep(sleep_time)
                # time.sleep(0.5)

        def step(self):
            """Lets the robot take one step"""
            # test
            print("test: function step executed..")

            speed = 200
            sleep_time = 0.01
            if self.direction == 1:
                # self.move_servo(self.servos[1], 150, speed)
                # self.move_servo(self.servos[2], 150, speed)
                # time.sleep(0.5)

                self.move_servo(self.servos[0], 400, speed)
                time.sleep(sleep_time)
                self.move_servo(self.servos[1], 400, speed)
                time.sleep(sleep_time)
                self.move_servo(self.servos[2], 400, speed)
                time.sleep(sleep_time)
                self.direction = 0
            elif self.direction == 0:
                if self.num_legs == 2:
                    self.move_servo(self.servos[0], 300, speed)
                    time.sleep(sleep_time)
                    self.move_servo(self.servos[1], 400, speed)
                    time.sleep(sleep_time)
                    self.move_servo(self.servos[2], 400, speed)
                    time.sleep(sleep_time)
                else:
                    self.move_servo(self.servos[0], 500, speed)
                    time.sleep(sleep_time)
                    self.move_servo(self.servos[1], 400, speed)
                    time.sleep(sleep_time)
                    self.move_servo(self.servos[2], 400, speed)
                    time.sleep(sleep_time)

                self.direction = 1

        def reset(self):
            """Puts the robot in its standard position"""
            sleep_time = 0.01
            self.move_servo(self.servos[0], 350, 200)
            time.sleep(sleep_time)
            self.move_servo(self.servos[1], 400, 200)
            time.sleep(sleep_time)
            self.move_servo(self.servos[2], 400, 200)
            time.sleep(sleep_time)
            time.sleep(0.1)


class ArmControls(Observable):
    """Manages arm controls"""

    def __init__(self):
        """Init"""
        super().__init__()
        print("class: ArmControls created.")

    def notifyObservers(self, arg=None):
        """Notifies the observers"""
        self.setChanged()
        Observable.notifyObservers(self, arg)

    def command(self):
        pass

    def move_x(self):
        pass

    def move_y(self):
        pass

    def move_z(self):
        pass

    def open_claw(self):
        pass

    def close_claw(self):
        pass

    def rotate_claw(self):
        pass
