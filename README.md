# Machine à lire
an open-source old newspapers distributor, a project by ALCA Nouvelle-Aquitaine derived from the project "L'Exprimante". 📃

**V2 Major Changes:** Markdown frontmatter syntax, multi-collection support, centralized configuration system, improved metadata validation, and web-based collection management.

## Ideas for future improvements

- displaying a notification to manually validate if the usb key action is performed.

## Tutorials (in FR)

- [Tutoriel d'utilisation pour les éditeurs sous forme de ticket prêt à coller dans la clé ajout](./doc/example-tutoriel.txt)
- [Un format de ticket vide (remplacez les textes entre double crochets `[[...]]`, le texte lorem ipsum correspond au contenu)](./doc/example-vide.txt)
- [dupliquer la makina](./doc/dupliquer-makina.md)
- [ajouter et supprimer des textes](./doc/ajouter-supprimer-textes.md)

## Admin tips
- Plug a keyboard and press `alt+f4` to exit Kiosk mode
  - You can now activate wifi again and access it remotely

- To edit the code more confortably directly on the raspberry you can install `samba` :
  - `sudo apt update`
  - `sudo apt-get install samba`
  - Change the workgroup name to the name of your workgroup & add windows support if needed :
    - ```
      workgroup = MYWORKGROUP
      wins support = yes
      ```
    - add this at the end :
      ```
      [pishare]
        comment = Pi Shared Folder
        path = /home/pi/Documents
        browsable = yes
        guest ok = yes
        writable = yes
      ```
  - make the document folder editable : `chmod 777 /home/pi/Documents -R`
  - restart samba : `sudo /etc/init.d/smbd restart`

## Some modifications applied

### Activate notifications
- Deactivate native modal when a usb is plugged : go to `files > édition > préférences > gestion des supports amovibles > décocher "Afficher les options disponibles pour les supports amovibles quand ils sont insérés"`
- Install the notification daemon `sudo apt-get install notification-daemon`
- Install spi2 `sudo apt-get install at-spi2-core`
- Add it to the list of services :
  - `cd /usr/share/dbus-1/services`
  - `sudo nano org.freedesktop.Notifications.service`
  - paste this : 
    ```
    [D-BUS Service]
    Name=org.freedesktop.Notifications
    Exec=/usr/lib/notification-daemon/notification-daemon
    ```
  - save and exit
- You might also need to install `libnotify-bin` : `sudo apt-get install libnotify-bin`

### Add webserver
- Install flask `sudo pip install flask`
- follow the same process used for `copy.service` (end of readme) with webserver.service

### V2: Switch to md with frontmatter syntax (Required for V2)
- Install frontmatter library: `pip3 install python-frontmatter`
- Install PyYAML for config parsing: `pip3 install PyYAML`

### Launch kiosque mode
Source : https://developers.deepgram.com/blog/2022/01/chromium-kiosk-pi/

- `sudo nano /etc/xdg/lxsession/LXDE-pi/autostart`
- This will open a new text file which will be executed when the desktop environment (LXDE) launches. In the file type the following:
```
@lxpanel --profile LXDE-pi
@pcmanfm --desktop --profile LXDE-pi

@xset s off
@xset -dpms
@xset s noblank

@chromium-browser --kiosk http://localhost:8888/
```

### Add images
- Create an "image" folder on the usb drive
- add an IMAGE text followed by the file name (without space !)

## V2 Configuration & Collections System

### Collections

Machine à lire V2 organizes articles into **collections**—independent groups with their own metadata, configuration, and visual identity.

### Configuration Files

**Global Config** (`AJOUT/Collections/config.yml`):
```yaml
changementCollectionPossible: true  # Allow visitors to switch collections
collectionParDefaut: "autrices"     # Auto-load collection on startup (can be false)
texteChoixCollection: "Choose..."   # UI text
imprimante: TM-T20III               # Printer model, TM-T20III or TM-T20IV
```

**Per-Collection Config** (`AJOUT/Collections/{collection}/config.yml`):
```yaml
collectionNom: Autrices
collectionDescription: "A collection of..."
collectionLogos:
  - logo.png
ticketDescription: "Text for tickets..."
ticketAvertissement: "Warning text..."
ticketLogos1:
  - logo-institution.png
ticketMentionsLegales: "Copyright..."
ticketLogos2:
  - logo-partner.png
```

These files should be provided on a USB key in the `AJOUT` folder to customize the system.

### USB Workflow (AJOUT/SUPPR)

**AJOUT (Add/Update Articles):**
- Rename USB key to `AJOUT`
- Create `Collections` folder
- Put the global config file at its root (see "Configuration Files")
- Create a folder for each collection (no space or special characters)
- Include `articles/` subfolder with article images (`Collections/{collectionName}/articles/001.md`, `002.md`, etc.)
- Include `images/` subfolder with article images
- Include the collection config on the same level (see "Configuration Files")
- Insert into Raspberry Pi → automatic processing (can take several minutes depending on the amount of articles)
- **Articles are merged** with existing content (not replaced)
- **⚠️ Remove USB key after processing** or it will re-process on reboot

**SUPPR (Delete All):**
- Use a **different USB key** named `SUPPR`
- Include empty file `suppression.txt` at root
- Insert into Raspberry Pi → deletes all articles and images
- **WARNING: Irreversible operation**
- **⚠️ Remove USB key after processing** or it will re-process on reboot

### Processing Pipeline

1. USB detected (AJOUT or SUPPR name)
2. `file_converter.py` orchestrates processing
3. `meta_extractor.py` parses frontmatter & validates metadata
4. `qrcodegenerator.py` creates QR codes for URLs
5. `txt_to_html.py` converts markdown to HTML
6. `imgkit` (wkhtmltopdf) renders HTML to JPG with footer
7. `images/{collection}/` stores final JPGs and metadata
8. `server.py` (Flask) serves web UI to display articles
9. `print.py` controls thermal printer output

Errors are logged to `images/errors_YYYY-MM-DD_HH-MM-SS.json`

## Original project (& V2 tweaks for file format)

this project was
  - initiated by Auvergne-Rhône-Alpes Livre et Lecture (Alizé Buisse and Priscille Legros)
  - created, designed and developed by Léa Belzunces, Esther Bouquet and Déborah-Loïs Séry
  - Is now transformed and reshaped by Rachel Pellin ([webtopie](https://webtopie.fr)) for ALCA Nouvelle-Aquitaine

V2 enhancements: Multi-collection support, YAML frontmatter metadata, improved validation, centralized configuration.

All of the next steps have been developed for a Raspberry Pi 4 running [Bullseye Version 11](https://downloads.raspberrypi.com/rpd_x86/images/rpd_x86-2022-07-04/2022-07-01-raspios-bullseye-i386.iso) and an Epson TM-T20III OR Epson TM-T20IV.

### V2: Article Format (Markdown with YAML Frontmatter)

Articles are now created as **Markdown files with YAML frontmatter** (the file extension can be .txt or .md, whichever suits you the most). Each article must follow this structure:

```markdown
---
titre: "My great article"
auteur: "Jane Doe"
categorie: "XVIII century"
url: https://url-for-the-qr_code.com
image: image-filename.jpg
bio: |-
  Optional author biography
  must have the weird "|-" on first line
  and each new line must be indented (for exemple with 2 spaces or a tab)
---

Regular markdown formatted text...

with paragraphs

and carriage returns<br>
very useful for poems

## You may insert subtitles

— or perhaps<br>
— some dialogs

```

**Required fields:** `titre`, `auteur`, `categorie`, `url`  
**Optional fields:** `image` (JPG/PNG), `bio` (multi-line)

**Important:** No accents in field names or filenames. Use `categorie` not `catégorie`, and `Portrait_Andre_Leo.jpg` not `Portrait d'André Léo.jpg`.

Images referenced in the `image:` field must be placed in a `images/` subfolder within the collection directory.

## 💿 install [python-escpos - Python library to manipulate ESC/POS Printers](https://python-escpos.readthedocs.io/en/latest/user/installation.html)
  
  - open your terminal
  
  - install dependencies: `sudo apt-get install python3 python3-setuptools python3-pip libjpeg8-dev`
  
  - write `sudo pip3 install python-escpos`
    - if you have a MemoryError, try to run `pip3` with `--no-cache-dir` such as `pip3 --no-cache-dir install python-escpos` but you should not need it
    - NB: sudo is very important if you want to run your script with systemd, otherwise you can't communicate to the usb with the root priviledge
    
  - plug the usb cable of the thermal printer into the raspberry and turn the thermal printer on

  - get the Product ID and Vendor ID using `lsusb` command
    - you should have something like: `Bus 001 Device 007: ID 04b8:0e28 Seiko Epson Corp.` <br>
      The part that interests us is `ID 04b8:0e28` where `04b8` is the vendor ID and `0e28` is the product ID
    
  - create the `udev` rule file with `sudo nano /etc/udev/rules.d/99-escpos.rules` 
    - write `SUBSYSTEM=="usb", ATTRS{idVendor}=="04b8", ATTRS{idProduct}=="0e28", MODE="0664", GROUP="dialout"` where you replace `04b8` and `0e28` by your own ID
    
  - use the `groups` command line to check which groups you're part of
    - and add your username to the `dialout` group if you're not. <br>
      `echo $USER` <br>
      `sudo adduser $USER dialout` where `$USER` is the name that appeared when you did the previous command
      
  - restart `udev` with the command `sudo udevadm control --reload` (or) `sudo service udev restart`
  - reboot your raspberry

## 📠 test your printer <> raspberry connection

  - open your terminal
  
  - create a new project folder using `mkdir nameofyourfolder`
  
  - go inside using `cd nameofyourfolder`
  
  - when you are in, write `touch nameofyourfile.py`
  
  - and write `sudo nano nameofyourfile.py` (will open the file and let you write inside of it) 
    - inside the file, you can copy paste this snippet of code: <br>
    
      ```python
      from escpos.printer import Usb 
      
      p = Usb(0x04b8, 0x0e28, 0)
      p.text("hello human, i wish u a nice day\n")
      p.cut() 
      ``` 
      📢 in `p = Usb(0x04b8, 0x0e28, 0)` you need to replace `04b8` and `0e28`by your own vendor and product ID.
  
  - save the file and exit it
  
  - make sure the printer is plugged correctly
  
  - run `python3 nameofyourfile.py`
  
  if the installation worked, you should now have a tiny printed paper greeting you 🔖 otherwise, you can find more information [here (raspi doc)](https://python-escpos.readthedocs.io/en/latest/user/raspi.html), or [here (original github repo)](https://github.com/python-escpos/python-escpos).
  
## 💻 customize print speed and density

- turn the printer on while pushing the feed button

  - it prints a test

- press the feed button again for more than 1 sec 

  - Mode Selection opens
  
  - press shortly (<1 sec)three times the feed button and one time long (>1 sec) the feed button
  
    - it opens Customize Value Settings
    
      - press three times to open the density options and one time long (>1 sec) the feed button
      
        - press three times to select density +2 and one time long (>1 sec) the feed button
        
      - press four times to open the speeed options and one time long (>1 sec) the feed button
      
        - press eleven times to select speed 11 and one time long (>1 sec) the feed button
        
- turn the printer off and restart it to use it

## 💻 try the code

  - open your terminal
  
  - check for updates `sudo apt-get update`

  - install wkhtmltopdf with qt patched (we need it to use `imgkit`): 
    ```bash
    sudo apt-get install xvfb
    wget https://github.com/wkhtmltopdf/packaging/releases/download/0.12.6-1/wkhtmltox_0.12.6-1.raspberrypi.stretch_armhf.deb 
    sudo apt-get install ./wkhtmltox_0.12.6-1.raspberrypi.stretch_armhf.deb 
    pip install coverage
    ```
    📢 If you are not using Stretch, go [here](https://wkhtmltopdf.org/downloads.html) and replace `wkhtmltox_0.12.6-1.raspberrypi.stretch_armhf.deb` with the right architecture for your distribution). 

  - install dependencies: `sudo apt-get install python3-markdown` and `pip3 install imgkit`

  - install dependency `pip3 install pyqrcode` and module `pip3 install pypng`

  - use `sudo apt install inotify-tools` so we can detect the usb drive later
  
  - clone this repository using git in ./Documents/ and your ssh key OR download it on your raspberry in ./Documents/ with `git clone https://github.com/estherbouquet/machine-a-lire`
  - Once it is cloned, go to ./machine-a-lire/
  - install bash dependency `sudo apt-get install recode` and allow privileges by copying `chmod u=rwx encoding.sh` in the terminal and then `chmod u=rwx listeningForPushedButton.sh` and `chmod u=rwx copy_from_usb.sh`, `chmod u=rwx delete_from_usb.sh` and finally `chmod u=rwx listeningForUSB.sh`.
 
- Render the fonts in the output result:
    - open the file explorer and go to `home/pi`
    - create a new folder named `.fonts`
    - make it visible with `ctrl+h`
    - copy the fonts in `home/pi/Documents/machine-a-lire/assets/` to `home/pi/Documents/.fonts`.
 
  - if you want to check manually that the program works first before running it independently when the raspberry starts:
    - be sure to be in the `machine-a-lire` folder.
    - write `python3 listeningForUSB.py` in the terminal. It will start listening for a USB named 'ajout' being plugged into the raspberry
    - plug the usb drive with a folder named `articles` (inside of which you will have the articles you want to copy to the raspberry for a later print)
      - `./listeningForUSB.sh` is now supposed to launch `./copy_from_usb.sh` (will copy the content of ./articles/ and convert it)
        - if the red led is blinking eight times quickly, it means that there is no folder named `articles` detected
        - if the green led is turning on it means that the program is working
          - the blue led will turn on when all the files are copied (you can remove safely your usb at this moment)
          - when the conversion is done, the green and blue led will turn off and the green led will blink one last time
    - open a new terminal window, go back to `./Documents/machine-a-lire/`
    - write `./listeningForPushedButton.sh` in the terminal and press the physical button whenever you feel ready
      - the led will blink twice if the program can find articles to print through the printer
    - whenever you want to stop/quit, just close the 2 terminal windows.

  - after you have checked that the two programs work when they are launched manually, you can run them automatically when the raspberry starts following the instructions below.

## 🎢 automatize

It is important that you check if your programs run flawlessly when you launch them manually before starting automatizing them. 
We are going to create 2 `.service` files because we are going to use `systemd`.

- Do `cd /etc/systemd/system`

### For copy.service
- `sudo nano copy.service`
  - copy paste the content of `copy.service` that you can find in the `/home/pi/Documents/machine-a-lire/systemdfiles` folder 
  - you can uncomment `StandardOutput=inherit` and comment `StandardOuput=null` to be able to track errors
  - `ctrl + o` to write then press `enter` to valid the modifications then `ctrl + x` to exit
  - you can check if it worked by using the command `cat copy.service`
📢 Everytime you need to do changes in this service file, don't forget to do `sudo systemctl daemon-reload` so the changes are taken into account
- `sudo systemctl start copy.service`
- you can check the status of the service (i.e. if it works) by typing `systemctl status copy.service` (and use `ctrl + c` to exit if necessary)
  - if it works correctly, a green "active" should appear in the terminal
  - you can use `sudo journalctl -u copy.service` to log errors
  - you can plug your usb. The green and then the yellow led should turn on
  - if no errors are raised in the status mode when you plug the usb, it means that the program is working for far. Congrats!
  - if no errors are encountered, the led will turn off meaning that the copy and conversion of the articles are over
  - don't forget to uncomment/comment back `StandardOutput` when you are sure the program is working
  - do a `sudo systemctl daemon-reload` so the changes are taken into account
 - now, we can enable the service so it will run our program as soon as the raspberry boots. To do so:
  - `sudo systemctl enable copy.service`
  - `sudo reboot` and try to plug a usb drive when the raspberry is up and running!
  - know that if one day you want to disable the `copy.service`, nothing simpler than `sudo systemctl disable copy.service`

### For printer.service
- `sudo nano printer.service`
  - copy paste the content of `printer.service` that you can find in the `/home/pi/Documents/machine-a-lire/systemdfiles` folder 
  - `ctrl + o` to write then press `enter` to valid the modifications then `ctrl + x` to exit
  - you can uncomment `StandardOutput=inherit` and comment `StandardOuput=null` to be able to track errors
  - do a `sudo systemctl daemon-reload` so the changes are taken into account
  - you can check if it worked by using the command `cat printer.service`
- `sudo systemctl start printer.service`
- you can check the status of the service (i.e. if it works) by typing `systemctl status printer.service` (and use `ctrl + c` to exit if necessary)
  - if it works correctly, a green "active" should appear in the terminal
  - you can use `sudo journalctl -u printer.service` to log errors
  - you can try to press the button. The blue led should blink twice and the printer print
  - if no errors are raised in the status mode when you push the button, it means that the program is working. Congrats!
  - uncomment/comment back the `StandardOutput` lines
  - do a `sudo systemctl daemon-reload` so the changes are taken into account
 - now, we can enable the service so it will run our program as soon as the raspberry boots. To do so:
  - `sudo systemctl enable printer.service`
  - `sudo reboot` and try to press the button when the raspberry starts up!
  - know that if one day you want to disable the `printer.service`, nothing simpler than `sudo systemctl disable printer.service`

And now you're done! 🎉 Enjoy!
