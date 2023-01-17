# SDA
2022 Projet de Structure des données avancées 
KIM TAEYEON (12204842)

## 1. Exécution
### 1) Les options
--dotpath : Si vous avez déjà une graphe sous forme de .dot, mettez le nom de chemin.</br>
--savepath : Mettez le nom de chemin où vous voulez sauvegarder des résultats (images).</br>
--octettree : Si vous voulez utilisez une structure d'octet tree, mettez cette option.</br>
--maxiter 300 : Mettez le nombre d'itérations (300 par défaut) </br></br>
--repulsiontype Eades : Indiquez le type de la force de repulsion. On a 3 choix ['Eades', 'FR', 'RepulsionbyDegree']</br>
--repulsioncons : 10 par défaut </br>
--repulsionideal : 10 par défaut (précisez si vous avez choisi FR)</br></br>
--attractiontype Eades : Indiquez le type de la force d'attraction. On a 4 choix ['Eades', 'FR',  'Normal', 'Linlog']</br>
--attractioncons : 100 par défaut </br>
--attractionideal : 0.1 par défaut (précisez si vous avez choisi FR)</br></br>
--draw : Utilisez cette option pour tracer des graphes par chaque iter.</br>
--nombrenode : Mettez un chiffre indiquant le nombre de noeuds dans le cas où vous n'utiliserez pas dotpath et utiliserez une graphe que vous définissez. !Attention, quand vous utilisez l'option --dotpath il faut mettre 0 sur l'option --nombrenode !</br>
--memoryusage : 'Utilisez cette option pour constater l utilisation de mémoire'

### 2) détails des options
#### (1) 'FR' signifie Fruchterman & Reingold théorie
#### (2) Il faut bien choisir le type de la force de repulsion et d'attraction. Si vous choisissez 'Eades' comme repulsion vous êtes obligé à choisir 'Eades' comme attraction. Si vous choisissez 'FR' comme repulsion vous êtes obligé à choisir 'FR' comme attraction. Si vous choisissez 'RepulsionbyDegree' comme repulsion vous êtes obligé à choisir 'Normal' ou 'Linlog' comme attraction.

### 3) Exemple
python main.py </br>
--dotpath "/Users/taeyeon/PycharmProjects/sda_projet/Molecules/benzène.dot"</br>
--savepath "/Users/taeyeon/PycharmProjects/sda_projet/pos_change/"</br>
--octettree </br>
--maxiter 300 </br>
--repulsiontype "Eades" </br>
--repulsioncons 10
--repulsionideal 10 </br>
--attractiontype "Eades" </br>
--attractioncons 100 </br>
--attractionideal 0.1 </br>
--draw </br>
--nombrenode 0</br>
--memoryusage
