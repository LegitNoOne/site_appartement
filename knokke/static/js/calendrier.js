function change_color_setup(jours_reserves) {
    var tags =document.getElementsByTagName("p");
    var annee=document.getElementById("titre").textContent;
    var mois=document.getElementById("titre_mois").textContent;
    mois=mois.replace(" ","")
    var compteur_memoire=document.getElementById("compteur_memoire").textContent;
    compteur_memoire=compteur_memoire*1
    var prix_memoire=document.getElementById("prix_memoire").textContent;
    prix_memoire=prix_memoire*1
//bloucle qui se charge de mettre la couleur verte (indispensable)

    //auto scroll vers le bas
    window.scroll(0,2500)
    
	for (var i=0;i<tags.length;i++){
        tags[i].style.color="green";

    }
//boucle qui va détecter les jours deja reserves et les mettre en rouge

    for (var i=0;i<tags.length;i++){

    	if (jours_reserves.indexOf(tags[i].textContent + mois + annee) != -1 ) {
        	tags[i].style.color="red";

        }
        
    }
    //empeche que les jours precedents le mois en cours ne puissent etre sélectionnés
    for (var i=0;i<tags.length;i++){
    	if(tags[i].textContent == ' '){
    		tags[i].onclick = function(){
    			
    		}
    	}
    }
    if (compteur_memoire != 0){
    	for (var i=0;i<tags.length;i++){
    		if (tags[i].textContent == 1) {
    			changecolor(tags[i])
    		}
    	}
    }
    
    
}

function changecolor(id) {
	var compteur=0
//boucle qui compte grace a la couleur bleue les jours sélectionnés
	var tags =document.getElementsByTagName("p");
	var liste_prix = document.getElementById("liste_prix").textContent;
	liste_prix=liste_prix.split(",")
	var liste_reduction = document.getElementById("liste_reduction").textContent;
	liste_reduction=liste_reduction.split(",")
	var reduction=100
	var compteur_prix = 0
	var tags_prix=[]
	var compteur_memoire=document.getElementById("compteur_memoire").textContent;
    compteur_memoire=compteur_memoire*1
    var prix_memoire=document.getElementById("prix_memoire").textContent;
    prix_memoire=prix_memoire*1
    
	//Creation de la liste pour definir les prix
	for (var i=0;i<tags.length-1;i++){
		
        if (tags[i].textContent!=' ') {
        	tags_prix.push(tags[i])
        }

    }
    
	compteur=Compteur()
//changement de couleur au click et refresh du message en dessous du calendrier
	var text_debut= 'Vous avez sélectionné '
	var text_sing= ' jour'
	var text_plu=' jours'
	if (id.style.color == "green") {
		id.style.color="blue";
		compteur++

		if (compteur==0) {

			compteur_prix=0
	    	
	    	compteur_prix=Prix(tags_prix,compteur_prix,liste_prix);
			document.getElementById("prix").innerHTML = "Vous n'avez pas n'avez pas sélectionné de date"
			document.getElementById("prix_total").innerHTML = compteur_prix + ' €'

		}
		if (compteur==1) {
			compteur_prix=0
	    		
	    	compteur_prix=Prix(tags_prix,compteur_prix,liste_prix);
	    	if ((compteur_memoire+compteur) >1){

	    		document.getElementById("prix").innerHTML = text_debut + (compteur+compteur_memoire)+ text_plu

	    	}
		    else {
		    	document.getElementById("prix").innerHTML = text_debut + (compteur+compteur_memoire)+ text_sing


		    }
		    reduction=Reduction(compteur, liste_reduction, compteur_prix);
	    	compteur_prix=((compteur_prix+prix_memoire)/100) * reduction;
	    	compteur_prix=Math.floor(compteur_prix);
		    document.getElementById("prix_total").innerHTML = compteur_prix + ' €'

		
	    }
	    if (compteur > 1){
	    	for (var i=0;i<tags.length;i++){
	    		if (tags[i] == id ){
	    			var fin_selection=i;
	    			
	    			
	    		}

	    		if (tags[i].style.color=="blue" && fin_selection != i ) {
	    			var debut_selection=i;
	    		    
	    		}
	    	}
	    	
	    //click apres la selection
	    	if (debut_selection<fin_selection){
	    		for (var i=debut_selection;i<fin_selection;i++){
	    			if (tags[i].style.color == 'red'){
	    				for (var i=i;i<tags.length;i--){
	    					if(i<0){break}
	    					if (tags[i].style.color != 'red'){
	    						tags[i].style.color='green'
	    					}
	    					}
	    				
	    				i=100
	    			}

	    			
	    			else {
	    				tags[i].style.color="blue";
	    			}
	    		}
	    	}
	    //click avant la selection
	    
	    	if (debut_selection>fin_selection){
	    		
	    		for (var i=fin_selection;i<debut_selection;i++){
	    			if (tags[i].style.color == 'red'){
	    				for (var i=i;i<tags.length;i++){
	    					if (tags[i].style.color != 'red'){
	    						tags[i].style.color='green'
	    					}
	    				}
	    				i=100

	    			}
	    			else{
	    			tags[i].style.color="blue";
	    		}

	    			}
	    		}
	    	//màj du compteur pour afficher le message correct en dessous du calendrier
	    	compteur=0
	    	compteur_prix=0
	    	compteur_prix=Prix(tags_prix,compteur_prix,liste_prix);

	    	compteur=Compteur()
	    	document.getElementById("prix_initial").innerHTML = compteur_prix
	    	if (compteur+compteur_memoire>1){
	    		document.getElementById("prix").innerHTML = text_debut + (compteur+compteur_memoire) + text_plu
	    	}
	    	else
	    	{
	    		document.getElementById("prix").innerHTML = text_debut + (compteur+compteur_memoire) + text_sing
	    	}

	    	//Applique une reduction aux prix et prix memoire additionnés pour que il y ait une justesse mathématique

	    	reduction=Reduction(compteur, liste_reduction, compteur_prix);
	    	compteur_prix=((compteur_prix+prix_memoire)/100) * reduction;

	    	compteur_prix=Math.floor(compteur_prix);
	    	document.getElementById("prix_total").innerHTML = compteur_prix + ' €'
	    	

	    }
	}
	
	else if (id.style.color=="blue") {
		id.style.color="green";
		compteur-=1

		var reponse=true
		if (compteur==0) {
			compteur_prix=0
	    	if (id.textContent == 1 && compteur_memoire != 0) {
	    		reponse=Popup_Selection()
	    		if (reponse==false){
	    			id.style.color='blue'
	    		}
	    		else {
	    			document.getElementById("compteur_memoire").textContent=0
	    			document.getElementById("prix_memoire").textContent=0
	    		}
	    	}
	    	compteur_prix=Prix(tags_prix,compteur_prix,liste_prix);
	    	if (reponse==true) {
			document.getElementById("prix").innerHTML = "Vous n'avez pas sélectionné de date"
			document.getElementById("prix_total").innerHTML = compteur_prix + ' €'
		    }
		    else{

		    	document.getElementById("prix").innerHTML = "Vous avez sélectionné " + (compteur+1+compteur_memoire) +" jours"
		    	//Applique une reduction aux prix et prix memoire additionnés pour que il y ait une justesse mathématique
		    	reduction=Reduction(compteur, liste_reduction, compteur_prix);
		    	compteur_prix=((compteur_prix+prix_memoire)/100) * reduction;
		    	compteur_prix=Math.floor(compteur_prix);
		    	document.getElementById("prix_total").innerHTML = compteur_prix + ' €'

		    }
		}
		if (compteur==1) {

			compteur_prix=0
	    	if (id.textContent == 1 && compteur_memoire != 0) {
	    		reponse=Popup_Selection()
	    		if (reponse==false){
	    			id.style.color='blue'
	    		}
	    		else {
	    			document.getElementById("compteur_memoire").textContent=0
	    			document.getElementById("prix_memoire").textContent=0
	    		}
	    	}
	    	compteur_prix=Prix(tags_prix,compteur_prix,liste_prix);
	    	if (reponse==true && compteur_memoire == 0) {
	    		
	    		document.getElementById("prix").innerHTML = "Vous avez sélectionné "+ compteur+" jour"
	    		document.getElementById("prix_total").innerHTML = compteur_prix + ' €'
		    }
		    else{
		    	
		    

	    	if ((compteur_memoire+compteur) >1) {
	    		document.getElementById("prix").innerHTML = text_debut + (compteur+compteur_memoire) + text_plu
	    	}
	    	else{
	    		document.getElementById("prix").innerHTML = text_debut + (compteur+compteur_memoire) + text_sing
	    	}
	    

		    //Applique une reduction aux prix et prix memoire additionnés pour que il y ait une justesse mathématique
		    reduction=Reduction(compteur, liste_reduction, compteur_prix);
	    	compteur_prix=((compteur_prix+prix_memoire)/100) * reduction;
	    	compteur_prix=Math.floor(compteur_prix);

		    document.getElementById("prix_total").innerHTML = compteur_prix + ' €'
		}
	    }
	    if (compteur > 1){
	    	var debut_selection=id.textContent;
	    	var debut =0;
	    	for (var i=0;i<tags.length;i++){
	    		if (tags[i].textContent == debut_selection) {
	    				i=100
	    			}
	    		else{
	    			debut++
	    		}

	    	}
	    	
	    	var compteur_debut_selection=0
	    	var compteur_fin_selection=0
	    	//obtenir le nombre de jours selectionnés avant le jours 'id'
	    	
	    	
	    	//obtenir le nombre de jours selectionnés apres le jours 'id'
	    	for (var i=debut_selection;i<tags.length;i++){
	    		if(tags[i].style.color=="blue"){
	    			compteur_fin_selection++
	    		}
	    	}
	    	//si le nombre de jours au debut est inferieur a ceux apres le jour 'id',
	    	//les jours au debut seront mis en vert sinon ca sera ceux a la fin ( else )
	    	for (var i=debut;i<tags.length;i++){
	    		if (tags[i].style.color != "red") {
	    			if (tags[i].textContent==1 && compteur_memoire !=0){
	    				reponse=Popup_Selection()
	    				if (reponse==false){
	    					tags[i].style.color='blue'

	    				}
	    				else {
	    					document.getElementById("compteur_memoire").textContent=0
	    					document.getElementById("prix_memoire").textContent=0
	    					tags[i].style.color="green"

	    				}
	    			}
	    			else {
	    				tags[i].style.color="green"
	    			}
	    		}
	    	}
	    			
	    			
	    		
	    	
	    	//màj du compteur pour afficher le message correct en dessous du calendrier
	    	compteur=0
	    	compteur_prix=0
	    	
	    	compteur_prix=Prix(tags_prix,compteur_prix,liste_prix);
	    	
	    	compteur=Compteur()
	    	document.getElementById("prix_initial").innerHTML = compteur_prix
	    	if (compteur+compteur_memoire>1){
	    		document.getElementById("prix").innerHTML = text_debut + (compteur+compteur_memoire) + text_plu
	    	}
	    	else {
	    		document.getElementById("prix").innerHTML = text_debut + (compteur+compteur_memoire) + text_sing
	    	}
	    	//Applique une reduction aux prix et prix memoire additionnés pour que il y ait une justesse mathématique
	    	
	    	reduction=Reduction(compteur, liste_reduction, compteur_prix);
	    	compteur_prix=((compteur_prix+prix_memoire)/100) * reduction;
	    	compteur_prix=Math.floor(compteur_prix);
	    	document.getElementById("prix_total").innerHTML = compteur_prix + ' €'


}
}
}

	  

//Fonction qui applique la reduction en pourcent et la renvoie

function Reduction(nb , liste_reduction, prix_total) {
	var reduction_memoire=document.getElementById("reduction_memoire");
	var reduction=-1
	var reduction_pourcent=100
	var compteur_memoire=document.getElementById("compteur_memoire").textContent;
    compteur_memoire=compteur_memoire*1
    nb=(nb+compteur_memoire);
	for (var a =0 ;a<liste_reduction.length-1; a+=2) {
		if (liste_reduction[a] - nb <=0 && reduction<liste_reduction[a]) {
			reduction=liste_reduction[a];
			reduction_pourcent=liste_reduction[a+1];
			reduction_pourcent=100-reduction_pourcent
	
		}
	}
	
	if (reduction_memoire.textContent != (100-reduction_pourcent) && reduction_memoire.textContent != 100 && reduction_memoire.textContent< (100-reduction_pourcent)){
		Afficher_Reduction(("Vous avez obtenu une réduction de "+ (100-reduction_pourcent) + "% !"));
	}
	if (reduction_memoire.textContent != (100-reduction_pourcent) && reduction_memoire.textContent != 100 && reduction_memoire.textContent> (100-reduction_pourcent)){
		Afficher_Reduction(("Vous avez diminué vers une réduction de "+ (100-reduction_pourcent) + "% en sélectionnant moins de jours !"));
	}
	reduction_memoire.textContent=(100-reduction_pourcent);
	return reduction_pourcent

}


function Liste_Memoire(next) {
	var tags =document.getElementsByTagName("p");
	var compteur=0
	var tags_prix=[]
	var liste_prix = document.getElementById("liste_prix").textContent;
	liste_prix=liste_prix.split(",")
	var compteur_memoire=document.getElementById("compteur_memoire").textContent;
    compteur_memoire=compteur_memoire*1
    var prix_memoire=document.getElementById("prix_memoire").textContent;
    prix_memoire=prix_memoire*1
    var premier_jour = document.getElementById("premier_jour").textContent;
    var annee=document.getElementById("titre").textContent;
    var mois=document.getElementById("titre_mois").textContent;
    //mise en memoire du premier jour de la selection tout en la supprimant si un jour deja reservé suit
    
    if (premier_jour == 0){
    	for (var i=0;i<tags.length;i++){
    		if (tags[i].style.color == "blue"){
    			premier_jour=tags[i].textContent;
    			for (var i=i;i<tags.length;i++){
    				if (tags[i].style.color == 'red'){
    					premier_jour=0
    					mois=''
    					annee=''
    				}
    			}
    			i=100

    		}
    	}
    }
    
    else{
    	mois= ''
    	annee=''
    }


    
	for (var i=0;i<tags.length-1;i++){
		
        if (tags[i].textContent!=' ') {
        	tags_prix.push(tags[i])
        }

    }

	for (var i=10;i<tags.length;i++){
        if (tags[i].textContent==' ') {
        	var dernier_id=tags[i-1]
        	i=100// met fin a la boucle
        	
        }
    }

	compteur=Compteur()
    var test_red=false
    var test_blue=false
    for (var i=0;i<tags.length;i++){
    	if (tags[i].style.color == 'blue') {
    		test_blue=true
    	}
    	if (tags[i].style.color == 'red' && test_blue==true) {

        		test_red=true
        	}
        }

    if (test_red==false && dernier_id.style.color == 'green' && compteur > 0) {	
    	changecolor(dernier_id);
    	}
    compteur=Compteur()
    prix=document.getElementById("prix_initial").textContent;

    if (prix == ''){
    	prix=0
    }
    prix=(prix*1)+prix_memoire
    compteur=compteur+compteur_memoire
    if (test_red==true){
    	prix=0;
    	compteur=0;
    }
    //Supression d'un bug qui ne supprimait pas la date du premier jour si aucun jour n'etait selectionné
    for (var i=0;i<premier_jour.length;i++){

    	if (premier_jour[i]== 0){
    		mois=''
    		annee=''
    	}
    }
    
	window.location = '/Henneaux_appartement/reservation/'+next+'/'+compteur+','+prix+'/'+premier_jour+mois+annee;
}


function Compteur (){
	var tags =document.getElementsByTagName("p");
	var compteur = 0
	for (var i=0;i<tags.length;i++){
        if (tags[i].style.color=="blue") {
        	compteur++
        }
    }
    return compteur
}

function Prix(tags_prix,compteur_prix,liste_prix){
	for (var i=0;i<tags_prix.length;i++){
		if (tags_prix[i].style.color=="blue") {
			compteur_prix=compteur_prix + (liste_prix[i] * 1)
		}
	}
	return compteur_prix
}

function Popup_Selection(){
	var reponse=confirm('Voulez-vous supprimer la sélection en cours ?')
	if (reponse == true){
		document.getElementById("premier_jour").textContent=0;
	}
	return reponse;
    
}



function Afficher_Reduction(reduction){
	// Get the modal
    var modal = document.getElementById('myModal');
    // Get the button that opens the modal
    var btn = document.getElementById("myBtn");
    // Get the <span> element that closes the modal
    var span = document.getElementsByClassName("close")[0];
    // When the user clicks the button, open the modal 
    var reduc = document.getElementsByClassName("reduction_popup")[0];
    reduc.textContent=reduction;
    modal.style.display = "block";
    
    // When the user clicks on <span> (x), close the modal
    span.onclick = function() {
    	modal.style.display = "none";
    }
    // When the user clicks anywhere outside of the modal, close it
    window.onclick = function(event) {
    	if (event.target == modal) {
    		modal.style.display = "none";
    	}
    }

    
}

function Formulaire (){
	var premier_jour = document.getElementById("premier_jour").textContent;
	var annee=document.getElementById("titre").textContent;
    var mois=document.getElementById("titre_mois").textContent;
	var tags =document.getElementsByTagName("p");
	if (premier_jour == 0){

		for (var i=0;i<tags.length;i++){
			if (tags[i].textContent == 1 && tags[i].style.color == 'blue'){
				premier_jour=tags[i].textContent+mois.replace(' ', '')+annee
			}
			else if (tags[i].style.color == 'blue' && tags[i-1].style.color != 'blue'){
				premier_jour=tags[i].textContent+mois.replace(' ', '')+annee
				
			}
		}
	}
	var dernier_jour = 0
	
    
    var prix=document.getElementById("prix_total").textContent;
    prix=prix.replace(' €', '')
	
	// definition du dernier jour de la selection 
	for (var i=0;i<tags.length;i++){
		if (tags[i].style.color == 'blue' && tags[i+1].style.color != 'blue'){
			dernier_jour=(tags[i].textContent + mois + annee)
			var nettoyage = 'oui'
			if (tags[i+1].style.color == 'red'){
				nettoyage='non'
			}
		}
	}
	var compteur_memoire=document.getElementById("compteur_memoire").textContent;
	var compteur=Compteur()
	compteur=(compteur*1+compteur_memoire*1)
	if (compteur>0){
		
	window.location = '/Henneaux_appartement/formulaire/'+premier_jour+'/'+dernier_jour+'/'+compteur+'/'+prix+'/'+nettoyage+'/';
	}
}