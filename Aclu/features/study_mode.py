
import json
import os


def study_mode():
    try:
        with open("/home/kali/Desktop/projects/Aclu/Aclu/features/config.json","r") as config_file:
            data = json.load(config_file)
            if data['isNightLightActivated']:
                os.system("redshift -x")
                data['isNightLightActivated'] = False
            else:
                os.system("redshift -o 2500")
                os.system("redshift -o 2500")
                os.system("redshift -o 2500")
                
                data['isNightLightActivated'] = True
        file = open("/home/kali/Desktop/projects/Aclu/Aclu/features/config.json", "w")
        file.write(json.dumps(data))

    except Exception as e:
        print('Error occured while reading config.json '+ str(e))
    
study_mode()
