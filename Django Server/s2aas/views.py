# Create your views here.
from django.http import HttpResponse
from django.shortcuts import render
from django.template import RequestContext
from s2aas.models import *
import datetime, sys
import time
from math import fsum
from twilio.rest import TwilioRestClient

account_sid = 'ACa7734d7ea9b332355e4a9b59cc77454c'
auth_token= 'f61facac65601e4ccf6c6cd520518e07'

#class main(object):	
def index(request):
    names=[]
    for naam in users.objects.all().values_list("name"):
        naam = naam[0].encode('utf-8')
        names.append(naam)
    now = datetime.datetime.now()
    context={'names':names, 'The time right now is: ':now}
    return render(request,'s2aas/show.html',context)

#def str_to_class(str):
#    return getattr(sys.modules[__name__], str)

def final(request):

    global selected_users
    selected_users=request.POST.getlist('users[]')
    print "Selected users:",selected_users
    global selected_sensors
    selected_sensors=request.POST.getlist('sensors[]')
    print "Selected sensors:", selected_sensors
    global selected_time
    selected_time=request.POST.getlist('Time[]')
    print "selected time:", selected_time
    global sensor_list,  timer
    sensor_list = []
    timer = []

    for sensors in selected_sensors: 
            sensor_list.append(str(sensors))
    
    for user in selected_users:
        w=users.objects.all().values_list("name", "users_cellnumber")
        for name, number in w:			
            if user == name:
                client = TwilioRestClient(account_sid, auth_token)
#                message = client.sms.messages.create(to=number, from_="+15305549648",
#                    body='S2AAS- Sensors requested: '+str(sensor_list))
    time.sleep(10)
    context={'selected_users':selected_users, 'selected_sensors':selected_sensors, 'selected_time':selected_time}
    return render(request,'s2aas/final.html',context)
    time.sleep(10)
    
def sent(request):
    

    for i in selected_time:
        if int(i) >=1:
            time_select = int(i)
        else:
            print "Enter some time range"
        
    for user in selected_users:
        q=users.objects.all().values_list("name", "users_cellnumber")
        for name, number in q:			
            if user == name:
            #	print user, name
                client = TwilioRestClient(account_sid, auth_token)
            #	print str(sensor_list)
                #message = client.sms.messages.create(to=number, from_="+15305549648",
                #body='S2AAS- Sensors requested: '+str(sensor_list))
                count =0
                while (count < time_select):
                    print time_select
                    
                    g_force_list = []
                    pressure_list = []
                    battery_list = []
                    light_list = []
                    thermometer_list = []
                    location_list = []
                    for sensor in sensor_list:
                          
                        if sensor == 'Accelerometer':
                            data = Accelerometer.objects.all().values_list( "users_cellnumber", "x", "y", "z").filter(users_cellnumber_id = number).order_by('-time')
                            for number, x, y ,z in data:
                                print  number, x, y, z
                                numerator = (x*x + y*y + z*z)
                                denominator = ( 9.8 * 9.8 )
                                g_force = numerator/denominator
                                g_force_list.append(g_force)
            
                        else:
                            g_force = 0
                        
                        if sensor == 'GPS':
                            data = gps.objects.all().values_list( "users_cellnumber", "x_axis", "y_axis").filter(users_cellnumber_id = number).order_by('-time')
                            for  number, x_axis, y_axis in data:
                                print number, x_axis, y_axis
                                location = x_axis + y_axis / 2
                                location_list.append(location)
                                if  location_list[0] != location_list[1]:
                                        location_int = '1'
                                else:
                                        location_int = '0'
                        else:
                             location = 0

                        if sensor == 'Barometer':
                            data = Barometer.objects.all().values_list( "users_cellnumber", "pressure").filter(users_cellnumber_id = number).order_by('-time')
                            for  number, pressure in data:
                                print number, pressure
                                pressure_list.append(pressure)
            
                        if sensor == 'Battery':
                            data = battery.objects.all().values_list( "users_cellnumber", "level").filter(users_cellnumber_id = number).order_by('-time')
                            for  number, level in data:
                                print  number, level
                                battery_list.append(level)

                        if sensor == 'Gyroscope':
                            data = Gyroscope.objects.all().values_list( "users_cellnumber", "x_ang", "y_ang", "z_ang").filter(users_cellnumber_id = number).order_by('-time')
                            for number, x_ang, y_ang ,z_ang in data:
                                print  number, x_ang, y_ang, z_ang

#                        if sensor == 'Magnetometer':
#                            data = Magnetometer.objects.all().values_list("users_cellnumber", "x_mag", "y_mag", "z_mag").filter#(users_cellnumber_id = number).order_by('-time')
#                            for  number, x_mag, y_mag ,z_mag in data:
#                                print  number, x_mag, y_mag, z_mag

                        if sensor == 'Linear_Accelerometer':
                            data = linear_acceleration.objects.all().values_list( "users_cellnumber", "x_LA", "y_LA", "z_LA").filter(users_cellnumber_id = number).order_by('-time')
                            for  number, x_LA, y_LA ,z_LA in data:
                                print  number, x_LA, y_LA, z_LA

                                            
                        if sensor == 'Rotational_Vector':
                            data = rotational_vector.objects.all().values_list( "users_cellnumber", "x_rot", "y_rot", "z_rot").filter(users_cellnumber_id = number).order_by('-time')
                            for  number, x_rot, y_rot ,z_rot in data:
                                print  number, x_rot, y_rot, z_rot
        
                        if sensor == 'Photometer':
                            data = Photometer.objects.all().values_list( "users_cellnumber", "ambient_light").filter(users_cellnumber_id = number).order_by('-time')
                            for  number, ambient_light in data:
                                print  number, ambient_light
                                light = ambient_light
                                light_list.append(light)
                                
                        else: 
                            light = 0

                        if sensor == 'Thermometer':
                            data = Ambient_temperature.objects.all().values_list( "users_cellnumber", "thermometer").filter(users_cellnumber_id = number).order_by('-time')
                            for  number, thermometer in data:
                                print  number, thermometer
                                thermometer_list.append(thermometer)

                        if sensor == 'Microphone':
                            data = microphone.objects.all().values_list("users_cellnumber", "sampleRateInHz", "channelConfig", "audioFormat").filter(users_cellnumber_id = number).order_by('-time')
                            for  number, sampleRateInHz, channelConfig, audioFormat in data:
                                print  number, sampleRateInHz, channelConfig, audioFormat 
                                volume = sampleRateInHz
                        else:
                            volume = 0

                    count = count +1
            
           	if len(g_force_list) > 0:
                	average_gforce = fsum(g_force_list)/len(g_force_list)
           	else:
                	average_gforce = g_force
            	if len(light_list) > 0:
                	average_light = fsum(light_list)/len(light_list)
            	else: 
                	average_light = light
            	if len(thermometer_list) > 0:          	    
                	average_thermometer = fsum(thermometer_list)/len(thermometer_list)
            	else:
                	average_thermometer = 10
            
            
            
          	if (average_gforce >= 2.0 and volume >= 10.0 and location_int = '1'):
                	print "The subscriber is driving"

            	elif average_gforce >= 2.0: # gps >= ? 
                	print "The subscriber is driving"
                
            	elif average_gforce <= .5 and  average_light <= 1 and volume <= 20:
                	print "The subscriber is sleeping"

            	elif average_light <= 1 and volume <= 20: # and gps >= ?:
                	print " The subscriber is sleeping"

            	elif average_light >= 1 and volume >= 20: # and gps
                	print " The subscriber woke up"

            	elif average_gforce >= .5 and average_light >= 1 and volume >= 20:
                	print " The susbcriber is awake"

            	elif average_gforce >= 1: #gps
                	print "The susbcriber is running"

            	elif average_gforce <= 1: #gps
                	print "The susbcriber is walking"

            	elif average_light >= 2 and volume >= 20 and average_gforce <= 1: #gps
                	print "The susbcriber is in a meeting"

            	elif average_gforce >= 3.5:
                	print " The subscriber had an accident "
                    
            	else:
                	print "cant predict any scenario using the sensors currently"

                    
        else:
            continue
    #context={'selected_users':selected_users, 'selected_sensors':selected_sensors }
    #return render(request,'s2aas/sent.html',context)
    
    for user in selected_users:
        w=users.objects.all().values_list("name", "users_cellnumber")
        for name, number in w:			
            if user == name:
                print "final message"
#                client = TwilioRestClient(account_sid, auth_token)
#                message = client.sms.messages.create(to=number, from_="+15305549648", 	body='S2AAS- stop sensing. ')
        

    context={'selected_users':selected_users, 'selected_sensors':selected_sensors }
    return render(request,'s2aas/sent.html',context)
    contect_instance = RequestContext(request)
    
    

