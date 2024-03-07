

# Add spacers to dock
 defaults write com.apple.dock persistent-apps -array-add '{tile-data={}; tile-type="spacer-tile";}'
 killall Dock #case sensitive

#Change screenshot format
 defaults write com.apple.screencapture type jpg

#Set system and display sleep
sudo systemsetup -getcomputersleep
sudo systemsetup -setcomputersleep xx or never
sudo systemsetup -getdisplaysleep
sudo systemsetup -setdisplaysleep xx or never