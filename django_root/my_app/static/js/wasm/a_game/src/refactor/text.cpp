#include <iostream>
#include <fstream>
#include "text.h"

// Function to print island asci art, and text that starts the game.
void ascisland(Player *obj)
{
	ifstream island("ASCI/island.txt");
	std ::cout << island.rdbuf();
	std ::cout << '\n';
	std ::cout << '\n';
	std ::cout << '\n';
	std ::cout << "You wake up to find youself alone on an island in the middle of the ocean.You can see a cruise ship on the horizon. " << '\n';
	std ::cout << '\n';
	std ::cout << "Attached the the island are three paths all going in the direction on the ship. No one path seems better than any other, which path will you choose?" << '\n';
}

/*Score function, Runs whenever the player dies/wins, IE when the game exits normally. */
void score(Player *obj)
{
	std ::cout << "\n         ||Score||         " << '\n';
	std ::cout << "===========================" << '\n';
	std ::cout << "# of Items: " << obj->items.size() << '\n';
	std ::cout << "# of Batteries: " << obj->getbatt() << '\n';
	std ::cout << "Distance Traveled: " << obj->getdelta() << '\n';
	if (obj->getsecr() != 1)
		std ::cout << "*Found a Secret*" << '\n';
	std ::cout << "===========================" << '\n';
	exit(1);
}

/* Death Fumction, runs when player hp has fallen to or below 0 */
void death(Player *obj)
{
	ifstream death("ASCI/death.txt");
	std ::cout << death.rdbuf();
	std ::cout << "\nYou crawl across the sand,no longer able to go on,your hands and feet bloodied from your journey; you feel the life slowly drain from your body as the sun beats down on you and the waves lap at the shore." << '\n';
	score(obj);
}

/* Victory function, runs when they player wins*/
void victory(Player *obj)
{
	ifstream victory("ASCI/victory.txt");
	std ::cout << victory.rdbuf();
	score(obj);
}

/* ASCI Art Functions uses input files to print ASCI art to the screen */
void asciwin()
{
	ifstream win("ASCI/win.txt");
	std ::cout << win.rdbuf();
}
void asciguardian()
{
	ifstream guardian("ASCI/guardian.txt");
	std ::cout << guardian.rdbuf();
}
void asciattack()
{
	ifstream attack("ASCI/attack.txt");
	std ::cout << attack.rdbuf();
}
void ascidodge()
{
	ifstream dodge("ASCI/dodge.txt");
	std ::cout << dodge.rdbuf();
}
void asciblock()
{
	ifstream blk("ASCI/block.txt");
	std ::cout << blk.rdbuf();
}
void ascigrab()
{
	ifstream grab("ASCI/grab.txt");
	std ::cout << grab.rdbuf();
}
void ascitree()
{
	ifstream tree("ASCI/tree.txt");
	std ::cout << tree.rdbuf();
}
void asciwell()
{
	ifstream well("ASCI/well.txt");
	std ::cout << well.rdbuf();
}
void ascimansion()
{
	ifstream mansion("ASCI/mansion.txt");
	std ::cout << mansion.rdbuf();
}
void ascicthulu()
{
	ifstream cthulu("ASCI/cthulu.txt");
	std ::cout << cthulu.rdbuf();
}
void ascilighthouse()
{
	ifstream lighthouse("ASCI/lighthouse.txt");
	std ::cout << lighthouse.rdbuf();
}
void ascibattlebox()
{
	ifstream box("ASCI/Sbox3.txt");
	std ::cout << box.rdbuf();
}
void asciwormholebox()
{
	ifstream box("ASCI/Sbox2.txt");
	std ::cout << box.rdbuf();
}
void ascibatterybox()
{
	ifstream box("ASCI/Sbox1.txt");
	std ::cout << box.rdbuf();
}
void ascistem()
{
	ifstream stem("ASCI/ameoba.txt");
	std ::cout << stem.rdbuf();
}
void ascimedkit()
{
	ifstream medkit("ASCI/medkit.txt");
	std ::cout << medkit.rdbuf();
}
void ascibandage()
{
	ifstream bandage("ASCI/bandage.txt");
	std ::cout << bandage.rdbuf();
}
void ascileather()
{
	ifstream leather("ASCI/leather.txt");
	std ::cout << leather.rdbuf();
}
void ascichainmail()
{
	ifstream chain("ASCI/chainmail.txt");
	std ::cout << chain.rdbuf();
}
void asciknight()
{
	ifstream knight("ASCI/knight.txt");
	std ::cout << knight.rdbuf();
}
void ascibulb()
{
	ifstream bulb("ASCI/bulb.txt");
	std ::cout << bulb.rdbuf();
}
void asciknife()
{
	ifstream knife("ASCI/knife.txt");
	std ::cout << knife.rdbuf();
}
void ascisword()
{
	ifstream sword("ASCI/sword.txt");
	std ::cout << sword.rdbuf();
}
void ascigun()
{
	ifstream gun("ASCI/gun.txt");
	std ::cout << gun.rdbuf();
}
void ascishop()
{
	ifstream shop("ASCI/shop.txt");
	std ::cout << shop.rdbuf();
}
void ascipirateship()
{
	ifstream ship("ASCI/pirateship.txt");
	std ::cout << ship.rdbuf();
}
void ascikey()
{
	ifstream key("ASCI/key.txt");
	std ::cout << key.rdbuf();
}
void ascisiren()
{
	ifstream siren("ASCI/siren.txt");
	std ::cout << siren.rdbuf();
}
void asciameoba()
{
	ifstream ameoba("ASCI/ameoba.txt");
	std ::cout << ameoba.rdbuf();
}
void ascialligator()
{
	ifstream alligator("ASCI/alligator.txt");
	std ::cout << alligator.rdbuf();
}
void ascioldman()
{
	ifstream oldman("ASCI/oldman.txt");
	std ::cout << oldman.rdbuf();
}
void ascikali()
{
	ifstream kali("ASCI/kali.txt");
	std ::cout << kali.rdbuf();
}
void ascicrabdragon()
{
	ifstream dragon("ASCI/crabdragon.txt");
	std ::cout << dragon.rdbuf();
}
void asciskeletonN()
{
	ifstream Askeleton("ASCI/Askeleton.txt");
	std ::cout << Askeleton.rdbuf();
}
void ascisquid()
{
	ifstream squid("ASCI/squid.txt");
	std ::cout << squid.rdbuf();
}
void ascipirate()
{
	ifstream pirate("ASCI/pirate.txt");
	std ::cout << pirate.rdbuf();
}
void ascicastaway()
{
	ifstream castaway("ASCI/castaway.txt");
	std ::cout << castaway.rdbuf();
}
void ascizombie()
{
	ifstream zombie("ASCI/zombie.txt");
	std ::cout << zombie.rdbuf();
}
void ascidolphin()
{
	ifstream dolphin("ASCI/dolphin.txt");
	std ::cout << dolphin.rdbuf();
}
void ascishark()
{
	ifstream shark("ASCI/shark.txt");
	std ::cout << shark.rdbuf();
}
void ascibox()
{
	ifstream box("ASCI/box.txt");
	std ::cout << box.rdbuf();
}
void ascilobster()
{
	ifstream lobster("ASCI/lobster.txt");
	std ::cout << lobster.rdbuf();
}
void asciskeleton()
{
	ifstream skeleton("ASCI/skeleton.txt");
	std ::cout << skeleton.rdbuf();
}
void asciwraith()
{
	ifstream wraith("ASCI/wraith.txt");
	std ::cout << wraith.rdbuf();
}