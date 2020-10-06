#include <iostream>
#include <string>
#include <fstream>
#include <sstream>

using namespace std;
int wczytajLiczby(string);
void sprawdzCzyZaprzyjaznione(int, int, string);
void zapiszDoPliku(int, int, bool, bool, string);

int main(int argc, char* argv[])
{
	string nazwaPliku = "";
	nazwaPliku += argv[1];
	
	wczytajLiczby(nazwaPliku);
	return 0;
}

int wczytajLiczby(string nazwa) {
	ifstream plikWejsciowy(nazwa);
	string wiersz;
	while (getline(plikWejsciowy, wiersz))
	{
		istringstream iss(wiersz);
		int a, b;
		if (!(iss >> a >> b)) { 
			zapiszDoPliku(0, 0, false, true, nazwa);
		}
		else {
			sprawdzCzyZaprzyjaznione(a, b, nazwa);
		}
	}
	plikWejsciowy.close();
	return 0;
}

void sprawdzCzyZaprzyjaznione(int liczbaA, int liczbaB, string nazwa) {
	int sumaDzielnikowA = 0, sumaDzielnikowB = 0;
	for (int i = 1; i < liczbaA; i++) {
		if (liczbaA % i == 0) {
			sumaDzielnikowA += i;
		}
	}
	for (int i = 1; i < liczbaB; i++) {
		if (liczbaB % i == 0) {
			sumaDzielnikowB += i;
		}
	}
	if (sumaDzielnikowA == liczbaB && sumaDzielnikowB == liczbaA) zapiszDoPliku(liczbaA, liczbaB, true, false, nazwa);
	else zapiszDoPliku(liczbaA, liczbaB, false, false, nazwa);
}

void zapiszDoPliku(int a, int b, bool czyZaprzyjaznione, bool czyError, string nazwa) {

	ofstream plikWyjsciowy;
	string toReplace("daneWejsciowe");
	size_t pos = nazwa.find(toReplace);
	nazwa.replace(pos, toReplace.length(), "daneWyjsciowe");
	plikWyjsciowy.open(nazwa, ios_base::app);

	if (czyError) {
		plikWyjsciowy << "b" << endl;
	}
	else {
		plikWyjsciowy << a << " ";
		plikWyjsciowy << b << " ";
		if(czyZaprzyjaznione) plikWyjsciowy << "t" << endl;
		else plikWyjsciowy << "n" << endl;
	}

	plikWyjsciowy.close();
}
