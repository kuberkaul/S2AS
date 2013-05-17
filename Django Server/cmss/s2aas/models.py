# s2aas/models.py
from django.db import models
from django.core.validators import MaxValueValidator, MinValueValidator


class MinMaxFloat(models.FloatField):
    def __init__(self, min_value=None, max_value=None, *args, **kwargs):
        self.min_value, self.max_value = min_value, max_value
        super(MinMaxFloat, self).__init__(*args, **kwargs)

    def formfield(self, **kwargs):
        defaults = {'min_value': self.min_value, 'max_value' : self.max_value}
        defaults.update(kwargs)
        return super(MinMaxFloat, self).formfield(**defaults)

class users(models.Model):
	id = models.AutoField(primary_key=True)
	name = models.CharField(max_length =200)
	users_cellnumber=models.CharField(max_length=10, unique=True)

class Accelerometer(models.Model):
	#cellnumbers=models.IntergerField(default=10, max_length=10)
	#permission=models.CharField(max_length=128)
	time=models.DateTimeField()
	users_cellnumber=models.ForeignKey(users, to_field = 'users_cellnumber')
	def save(self):
		self.uploaded_time=datetime.now()
		models.Model.save(self)
	x = models.FloatField(
    validators = [MinValueValidator(-100.00), MaxValueValidator(1000.00)])
	y = models.FloatField(
    validators = [MinValueValidator(-100.00), MaxValueValidator(1000.00)])
	z = models.FloatField(
    validators = [MinValueValidator(-100.00), MaxValueValidator(1000.00)])

#class Gravity_Sensor(models.Model):
#	#cellnumbers=models.IntergerField(default=10, max_length=10)
#	#permission=models.CharField(max_length=128)
#	time=models.DateTimeField()
#	users_cellnumber=models.ForeignKey(users, to_field = 'users_cellnumber')
#	def save(self):
#		self.uploaded_time=datetime.now()
#		models.Model.save(self)
#	x_gravity = models.FloatField(
#   validators = [MinValueValidator(-100.00), MaxValueValidator(1000.00)])
#	y_gravity = models.FloatField(
#    validators = [MinValueValidator(-100.00), MaxValueValidator(1000.00)])
#	z_gravity = models.FloatField(
 #   validators = [MinValueValidator(-100.00), MaxValueValidator(1000.00)])


#class Magnetometer(models.Model):
#	#cellnumbers=models.IntergerField(default=10, max_length=10)
#	#permission=models.CharField(max_length=128)
#	time = models.DateTimeField()
#	users_cellnumber=models.ForeignKey(users, to_field = 'users_cellnumber')
#	def save(self):
#		self.uploaded_time=datetime.now()
#		models.Model.save(self)
#	x_mag = models.FloatField(
 #   validators = [MinValueValidator(-100.00), MaxValueValidator(1000.00)])
#	y_mag = models.FloatField(
 #   validators = [MinValueValidator(-100.00), MaxValueValidator(1000.00)])
#	z_mag = models.FloatField(
 #   validators = [MinValueValidator(-100.00), MaxValueValidator(1000.00)])

class Gyroscope(models.Model):
	#cellnumbers=models.IntergerField(default=10, max_length=10)
	#permission=models.CharField(max_length=128)
	time=models.DateTimeField()
	users_cellnumber=models.ForeignKey(users, to_field = 'users_cellnumber')
	def save(self):
		self.uploaded_time=datetime.now()
		models.Model.save(self)
	x_ang = models.FloatField(
    validators = [MinValueValidator(-100.00), MaxValueValidator(1000.00)])
	y_ang = models.FloatField(
    validators = [MinValueValidator(-100.00), MaxValueValidator(1000.00)])
	z_ang = models.FloatField(
    validators = [MinValueValidator(-100.00), MaxValueValidator(1000.00)])


class Photometer(models.Model):
	
	ambient_light = models.FloatField(
    validators = [MinValueValidator(-100.00), MaxValueValidator(1000.00)])
	time = models.DateTimeField()
	users_cellnumber=models.ForeignKey(users, to_field = 'users_cellnumber')
	def save(self):
		self.uploaded_time1=datetime.now()
		models.Model.save(self)


class microphone(models.Model):
	#cellnumbers=models.IntergerField(default=10, max_length=10)
	#permission=models.CharField(max_length=128)
	time=models.DateTimeField()
	users_cellnumber=models.ForeignKey(users, to_field = 'users_cellnumber')
	def save(self):
		self.uploaded_time=datetime.now()
		models.Model.save(self)
	sampleRateInHz  = models.FloatField(
    validators = [MinValueValidator(-100.00), MaxValueValidator(1000.00)])
	channelConfig  = models.FloatField(
    validators = [MinValueValidator(-100.00), MaxValueValidator(1000.00)])
	audioFormat = models.FloatField(
    validators = [MinValueValidator(-100.00), MaxValueValidator(1000.00)])

class gps(models.Model):
	#cellnumbers=models.IntergerField(default=10, max_length=10)
	#permission=models.CharField(max_length=128)
	time=models.DateTimeField()
	users_cellnumber=models.ForeignKey(users, to_field = 'users_cellnumber')
	def save(self):
		self.uploaded_time=datetime.now()
		models.Model.save(self)
	x_axis  = models.FloatField(
    validators = [MinValueValidator(-100.00), MaxValueValidator(1000.00)])
	y_axis  = models.FloatField(
    validators = [MinValueValidator(-100.00), MaxValueValidator(1000.00)])


class Barometer(models.Model):
	
	pressure = models.FloatField(
    validators = [MinValueValidator(-100.00), MaxValueValidator(1000.00)])
	time = models.DateTimeField()
	users_cellnumber=models.ForeignKey(users, to_field = 'users_cellnumber')
	def save(self):
		self.uploaded_time1=datetime.now()
		models.Model.save(self)

class Proximity(models.Model):
	
	proximity = models.FloatField(
    validators = [MinValueValidator(-100.00), MaxValueValidator(1000.00)])
	time = models.DateTimeField()
	users_cellnumber=models.ForeignKey(users, to_field = 'users_cellnumber')
	def save(self):
		self.uploaded_time1=datetime.now()
		models.Model.save(self)


class rotational_vector(models.Model):
	#cellnumbers=models.IntergerField(default=10, max_length=10)
	#permission=models.CharField(max_length=128)
	time = models.DateTimeField()
	users_cellnumber=models.ForeignKey(users, to_field = 'users_cellnumber')
	def save(self):
		self.uploaded_time=datetime.now()
		models.Model.save(self)
	x_rot = models.FloatField(
    validators = [MinValueValidator(-100.00), MaxValueValidator(1000.00)])
	y_rot = models.FloatField(
    validators = [MinValueValidator(-100.00), MaxValueValidator(1000.00)])
	z_rot = models.FloatField(
    validators = [MinValueValidator(-100.00), MaxValueValidator(1000.00)])


class Humidity(models.Model):
	air_humidity = models.IntegerField(default=3, max_length=3)
	time = models.DateTimeField()
	users_cellnumber=models.ForeignKey(users, to_field = 'users_cellnumber')
	def save(self):
		self.uploaded_time1=datetime.now()
		models.Model.save(self)

class linear_acceleration(models.Model):
	#cellnumbers=models.IntergerField(default=10, max_length=10)
	#permission=models.CharField(max_length=128)
	time = models.DateTimeField()
	users_cellnumber=models.ForeignKey(users, to_field = 'users_cellnumber')
	def save(self):
		self.uploaded_time=datetime.now()
		models.Model.save(self)
	x_LA = models.FloatField(
    validators = [MinValueValidator(-100.00), MaxValueValidator(1000.00)])
	y_LA = models.FloatField(
    validators = [MinValueValidator(-100.00), MaxValueValidator(1000.00)])
	z_LA = models.FloatField(
    validators = [MinValueValidator(-100.00), MaxValueValidator(1000.00)])

class Ambient_temperature(models.Model):
	thermometer = models.IntegerField(default=3, max_length=3)
	time = models.DateTimeField()
	users_cellnumber=models.ForeignKey(users, to_field = 'users_cellnumber')
	def save(self):
		self.uploaded_time1=datetime.now()
		models.Model.save(self)

#class Orientation(models.Model):
#
#	#cellnumbers=models.IntergerField(default=10, max_length=10)
#	#permission=models.CharField(max_length=128)
#	time = models.DateTimeField()
#	users_cellnumber=models.ForeignKey(users, to_field = 'users_cellnumber')
#	def save(self):
#		self.uploaded_time=datetime.now()
#		models.Model.save(self)
#	x_pitchOr = models.FloatField(
 #   validators = [MinValueValidator(-180.00), MaxValueValidator(1000.00)])
#	x_rollOr = models.FloatField(
 #   validators = [MinValueValidator(-100.00), MaxValueValidator(1000.00)])
	
class contacts(models.Model):
	cellnumbers=models.CharField(max_length=10)
	users_cellnumber=models.ForeignKey(users, to_field = 'users_cellnumber')

class battery(models.Model):
	level = models.IntegerField(default=3, max_length=3)
	time = models.DateTimeField()
	users_cellnumber=models.ForeignKey(users, to_field = 'users_cellnumber')
	def save(self):
		self.uploaded_time1=datetime.now()
		models.Model.save(self)
	



