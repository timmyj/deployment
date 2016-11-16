from django.db import models

class machine(models.Model):
    
    hostname = models.CharField(
    	max_length=6,
    	unique=True,
    )

    installdate = models.DateField('Install Date')
    
    BIOS = 'BIOS'
    UEFI = 'UEFI'
    boot_mode_choice = (
    	(BIOS, 'BIOS'),
	(UEFI, 'UEFI'),
    )
    boot_mode = models.CharField(
        "Boot Mode",
	max_length=4,
	choices=boot_mode_choice,
	default=BIOS,
    )

    Desktop = 'Desktop'
    Laptop = 'Laptop'
    type_choice = (
        (Desktop, 'Desktop'),
        (Laptop, 'Laptop'),
    )
    machine_type = models.CharField(
        "Machine Type",
        choices=type_choice,
        default=Desktop,
        max_length=10,
    )
    
    x86 = 'x86'
    x64 = 'x64'
    archi_choice = (
        (x86, 'x86'),
        (x64, 'x64'),
    )
    architecture = models.CharField(
        "Architecture",
        choices=archi_choice,
        default=x64,
        max_length=3,
    )
    
    mac_address = models.CharField("MAC Address",max_length = 17,blank=False,unique=True)
    
    user = models.CharField(
       	"Assigned User",
        max_length=100,
        default="None",
    )
    
    manufacturer = models.CharField(
	"System Manufacturer",
	max_length=30,
	default="Unknown",
    )
    
    service_tag = models.CharField(
	"Service Tag",
	max_length=6,
	default="Unknown",
    )    
    
    cpu = models.CharField(
	"CPU",
	max_length=20,
	default="Unknown",
    )
        
    RAM = models.CharField(
	"RAM",
	max_length=10,
	default="Unknown",
    )
    
    def __str__(self):
        return self.hostname
