# COMMAND LINE WEATHER FORECASTING TOOL

## Introduction
- Displays the weather forecast using Open Weather API
- Can be used in command line
- Gets the input from the user as
   - City name
   - Latitude and Longitude
   - Automated IP Address
- Gets the input as Parse(switches)
- Checks for errors and returns appropriate exceptions


## Functionality
- Finds weather using city name
```zsh
 python weather.py chennai
 ```

- Finds the weather latitude and longitude
```zsh
python weather.py chennai -lat 65.876 -long 76.865
```

- Finds the weather using Automated IP Address
```zsh
python weather.py 
```

- Finds the weather using verbose mode
```zsh
python weather.py chennai -v 
```

- Help Menu
```zsh
python weather.py -h
```


## ARCHITECTURE OF THE MODEL
![image](https://github.com/Harishspice/Microsoft-Git-Copilot/assets/117935868/0ffcfaaf-cb8b-43a7-af8a-a679dd6eca7f)



### USING CITY NAME
![WhatsApp Image 2023-06-24 at 17 14 22](https://github.com/Harishspice/Microsoft-Git-Copilot/assets/117935868/5e350eec-b2fc-46f8-afa3-0c6359265c16)



### IN VERBOSE MODE 
![WhatsApp Image 2023-06-24 at 17 14 24](https://github.com/Harishspice/Microsoft-Git-Copilot/assets/117935868/cb279cc1-0f3d-4fbe-95c9-e81c6550497a)



### IN AUTOMATED MODE
![WhatsApp Image 2023-06-24 at 17 44 40](https://github.com/Harishspice/Microsoft-Git-Copilot/assets/117935868/715be4f8-188e-4207-9286-8f8bbb443024)

### HELP MENU
![WhatsApp Image 2023-06-24 at 17 46 21](https://github.com/Harishspice/Microsoft-Git-Copilot/assets/117935868/638e2878-f035-4a05-a502-b4a91e6b9125)

## License

This project is licensed under the GNU General Public License v3.0 License - see the [LICENSE](LICENSE) file for details.

## Acknowledgments

- Thanks to Github Copilot for providing a powerful foundation for this Tool.
- [Harishspice](https://github.com/Harishspice) has created and is maintaining this project.

## Contact

If you have any questions or suggestions regarding the Weather Forecasting Tool, feel free to contact me at @harishr.shankar@gmail.com.
