from abc import ABC,abstractmethod
class SmartDevice(ABC):
    def __init__(self,device_id,room):
        self._device_id=device_id
        self.room=room
        self.is_on=False
    @property
    def device_id(self):
        return self._device_id
    def check_if_on(self):
        return self.is_on
    @abstractmethod
    def toggle_power(self):
        pass
    @abstractmethod
    def get_status(self):
        pass
    def _validate_percentage(self,value,label):
        if not 0<=value<=100:
            print(f'Request Denied!!! for {value}% {label} Because [{self.device_id}]: {label} must be in range 0-100')
            return False
        return True
class SmartLight(SmartDevice):
    def __init__(self, device_id, room):
        super().__init__(device_id, room)
        self._brightness=0
        self.device_type='Light'
    def set_brightness(self,value):
        if self._validate_percentage(value,'Light Brightness'):
            self._brightness=value
            if value>0:
                self.is_on=True
            else:
                self.is_on=False
            print(f'Brightness Set to {self._brightness}% For Light at [{self.device_id}] in {self.room}')
    def get_brightness(self):
        return self._brightness
    def get_status(self):
        state='ON' if self.is_on else 'OFF'
        print(f'Device: Light | [Zone] : {self.device_id}  | Room: {self.room} | Power: {state:<3} | (Brightness: {self._brightness}%)  ')
    def toggle_power(self):
        self.is_on=not self.is_on
        if self.is_on:
            self._brightness=100
            print(f'Light [{self.device_id}] in {self.room} is ON')
        else:
            self._brightness=0
            print(f'Light [{self.device_id}] in {self.room} is OFF')
class SmartFan(SmartDevice):
    def __init__(self, device_id, room):
        super().__init__(device_id, room)
        self._speed=0
        self.device_type='Fan'
    def set_speed(self,value):
        if self._validate_percentage(value,'Fan Speed'):
            self._speed=value
            # if value>0:
            #     self.is_on=True
            # else:
            #     self.is_on=False
            self.is_on=value>0 
            print(f'Speed Set to {self._speed}% For Fan {self.device_id} in {self.room}')
    def get_speed(self):
        return f'The Current Speed of Fan is: {self._speed}%'
    def get_status(self):
        state='ON' if self.is_on else 'OFF'
        print(f'Device: Fan   | [Zone] : {self.device_id}  | Room: {self.room} | Power: {state:<3} | (Speed: {self._speed}%)       ')
    def toggle_power(self):
        self.is_on=not self.is_on
        if self.is_on:
            self._speed=100
            print(f'Fan [{self.device_id}] in {self.room} is ON')
        else:
            self._speed=0
            print(f'Fan [{self.device_id}] in {self.room}is OFF')
class SmartPlug(SmartDevice):
    def __init__(self, device_id, room):
        super().__init__(device_id, room)
        self._power_watts=0
        self.device_type='Plug'
    def set_load(self,watts):
        if watts >= 0:
            self._power_watts = watts
            self.is_on=watts>0
            print(f'Plug [{self.device_id}]  in {self.room} is now drawing {watts}W')
        else:
            print(f' Warning [{self.device_id}]: Request Denied!!! \n  Load cannot be negative')
    def get_load(self):
        return self._power_watts
    def get_status(self):
        state='ON' if self.is_on else 'OFF'
        print(f'Device: Plug  | [Zone] : {self.device_id} | Room: {self.room}  | Power: {state:<3} | (Load: {self._power_watts}W)')

    def toggle_power(self):
        self.is_on=not self.is_on
        self._power_watts = 0 if not self.is_on else 100
        print(f"Plug [{self.device_id}]  in {self.room} is {'ON' if self.is_on else 'OFF'} ")
class SmartLock(SmartDevice):
    def __init__(self, device_id, room):
        super().__init__(device_id, room)
        self.is_locked=True
        # self.is_on=True
        self.device_type='Lock'
    def lock(self):
        self.is_locked=True
        print(f'Lock [{self.device_id}] in {self.room} is LOCKED')
    def unlock(self):
        self.is_locked=False
        print(f'Lock [{self.device_id}] in {self.room} is UNLOCKED')
    def get_status(self):
        state='LOCKED' if self.is_locked else 'UNLOCKED'
        print(f'Device: Lock  | [Zone] : {self.device_id} | Room: {self.room}  | Status: {state}')
    def toggle_power(self):
        self.is_locked=not self.is_locked
        print(f"{self.device_id} Lock in {self.room} is now {'LOCKED' if self.is_locked else 'UNLOCKED'}")
class SmartHome:
    def __init__(self):
        self._devices=[]
    def add_device(self,device):
        for existing in self._devices:
            if existing.device_id==device.device_id:
                print('Device ID already exists!')
                return 
        self._devices.append(device)
        print(f'Device [{device.device_id}] added successfully')
    def remove_device(self,device_id):
        for device in self._devices:
            if device.device_id== device_id:
                self._devices.remove(device)
                print(f'Device [{device.device_id}] removed successfully')
                return 
        print('Device not found')
    def find_device(self,device_id):
        for device in self._devices:
            if device.device_id== device_id:
                return device
        return None
    def show_all_devices(self):
        if len(self._devices)==0:
            print('No devices available')
            return 
        print('\n======== ALL DEVICES =======')
        for device in self._devices:
            device.get_status()
        print('======================')
    def show_room_devices(self,room):
        found=False
        print(f'========= {room.upper()} =========')
        for device in self._devices:
            if device.room.lower()==room.lower():
                device.get_status()
                found=True
        if not found:
            print('No devices found in this room')
        print('==================================')
    def toggle_device(self,device_id):
        device=self.find_device(device_id)
        if device is None:
            print('Device not found')
            return 
        device.toggle_power()
    def turn_off_all(self):
        print('\n Turning OFF all devices \n')
        for device in self._devices:
            if device.device_type=='Lock':
                continue
            if device.is_on:
                device.toggle_power()
        print('\nAll applicable devices are OFF\n')
    def turn_on_all(self):
        print('\n Turning ON all devices \n')
        for device in self._devices:
            if device.device_type=='Lock':
                continue
            if not device.is_on:
                device.toggle_power()
        print('\nAll applicable devices are ON\n')
    def device_count(self):
        print(f'\nTotal Devices: {len(self._devices)}')
        return len(self._devices)
def add_device_menu(home):
    print('\n======= ADD DEVICES ======')
    print('1.Smart Light')
    print('2.Smart Fan')
    print('3.Smart Plug')
    print('4.Smart Lock')
    print('5.Back')
    choice=input('Enter choice: ')
    if choice=='5':
        return
    device_id=input('Enter Device ID: ')
    room=input('Enter Room Name: ')
    if choice=='1':
        device=SmartLight(device_id,room)
    elif choice=='2':
        device=SmartFan(device_id,room)
    elif choice=='3':
        device=SmartPlug(device_id,room)
    elif choice=='4':
        device=SmartLock(device_id,room)
    else:
        print('Invalid choice')
        return 
    home.add_device(device)
def main():
    home=SmartHome()
    home.add_device(SmartLight('Zone-A','Live Room'))
    home.add_device(SmartLight('Zone-M','Bed Room'))
    home.add_device(SmartFan('Fan-01','Bed Room'))
    home.add_device(SmartPlug('Plug-01','Balcony'))
    home.add_device(SmartPlug('Plug-02','Kitchen'))
    home.add_device(SmartLock('Lock-01','Front Door'))
    while True:
        print('\n==========================')
        print('SMART HOME MANAGEMENT SYSTEM')
        print('============================')
        print('1.Add Device')
        print('2.Remove Device')
        print('3.View all Devices')
        print('4.Control Device')
        print('5.View Room Devices')
        print('6.Turn ON ALL Devices')
        print('7.Turn OFF ALL Devices')
        print('8.Count Devices')
        print('9.Exit')
        print('====================================')
        choice=input('Enter your choice: ')
        if choice=='1':
            add_device_menu(home)
        elif choice=='2':
            device_id=input('Enter Device ID to remove: ')
            home.remove_device(device_id)
        elif choice=='3':
            home.show_all_devices()
        elif choice=='4':
            device_id=input('Enter Device ID: ')
            device=home.find_device(device_id)
            if device is None:
                print('Device not Found')
                continue
            print('\n====== CONTROL DEVICE ========')
            print('1.Toggle Power')
            if device.device_type=='Light':
                print('2.Set Brightness')
            elif device.device_type=='Fan':
                print('2.Set Speed')
            elif device.device_type=='Plug':
                print('2.Set Load')
            elif device.device_type=='Lock':
                print('2.Lock')
                print('3.Unlock')
            controlchoice=input('Enter choice: ')
            if controlchoice=='1':
                device.toggle_power()
            elif controlchoice=='2':
                if device.device_type=='Light':
                    value=int(input('Enter Brightness (0-100): '))
                    device.set_brightness(value)
                elif device.device_type=='Fan':
                    value=int(input('Enter Speed (0-100): '))
                    device.set_speed(value)
                elif device.device_type=='Plug':
                    value=int(input('Enter Load in watts:'))
                    device.set_load(value)
                elif device.device_type=='Lock':
                    device.lock()
            elif controlchoice=='3' and device.device_type=='Lock':
                device.unlock()
            else:
                print('Invalid Choice')
                
        elif choice=='5':
            room=input('Enter Room Name: ')
            home.show_room_devices(room)
        elif choice=='6':
            home.turn_on_all()
        elif choice=='7':
            home.turn_off_all()
        elif choice=='8':
            home.device_count()
        elif choice=='9':
            print('\nThank you for using Smart Home Management System!')
            break
        else:
            print('\n Invalid choice please try again!!')
if __name__ =="__main__":
    main()