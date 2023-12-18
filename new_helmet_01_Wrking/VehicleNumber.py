import BikeImageHandler
def getVehicleNUmber(imagepath):
    vehiclenumber=BikeImageHandler.getBikeNumber(imagepath)
    
    ## here we need to put anoop's code
   
    # vehiclenumber="MH 12 PY 6753"
    # vehiclenumber=vehiclenumber.replace(" ","")
    return vehiclenumber

if __name__ == '__main__':
    getVehicleNUmber()
    