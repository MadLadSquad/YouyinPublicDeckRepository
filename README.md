# YouyinPublicDeckRepository
A public repository where users of [youyin](https://youyin.madladsquad.com/) can upload their own decks for usage by the community. The decks here, will
be automatically added to the packages page of the website for others to consume once merged(may take more than 6 hours for the site to update)

## Contributing
To contribute a deck, first export one from the youyin website using the `Export` button on the `Deck` page as shown here:

![image](https://user-images.githubusercontent.com/40400590/217593295-56180588-8bd6-4565-9fe3-1596d9f7b6fc.png)

Next, create a [github account](https://github.com/)
![image](https://user-images.githubusercontent.com/40400590/218274570-1bb00a32-f98a-4a16-a751-8251ca446167.png)

After that you need to fork this repository
![image](https://user-images.githubusercontent.com/40400590/218274678-62b382b4-42d9-4517-9342-fb8eed4c453a.png)

Next, rename your saved file, remember that `-` will be replaced with ` ` so a deck named `kangxi-radicals.yydeck.json` will become `Kangxi Radicals`
on the marketplace page

After the files are renamed upload it under the `community` folder under the latest release.

When you're done simply create a pull request
![image](https://user-images.githubusercontent.com/40400590/218274855-b18e6ac1-079b-4384-a287-84a2a982e25b.png)

Here, create a descriptive title and description like this:
![image](https://user-images.githubusercontent.com/40400590/218274942-1fd10711-b0cd-408b-8fe4-e14954802bae.png)

and finally click submit. Make sure to monitor the pull request from a response from the maintainers. Once a pull request is approved and merged, changes
should apply in about 10 minutes

If you're submitting a deck that's already pre-leveled up and want to leave the data there(for example a deck where every card is set at level 3) you
should change the file extension of the deck from `.yydeck.json` to `.presetlvl.yydeck.json` and make sure the name of the deck represents it.
Not setting the file extension like this will result in the removal of all data once the automatic sanitizer goes trough your deck
