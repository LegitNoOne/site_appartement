function Set_Up(){
	var prix = document.getElementById("prix").textContent;
	prix=prix*1
	var nettoyage = document.getElementById("nettoyage_donnée").textContent;
	nettoyage=nettoyage*1
	var afficher_prix = document.getElementById("info4");
	var nettoyage_verification= document.getElementById("nettoyage_verification").textContent;
	if (nettoyage_verification == "non"){
		document.getElementById("id_nettoyage").style.display="none";
		document.getElementById("nettoyage_non").textContent="Nettoyage indisponible puisque le lendemain de votre départ, le jour est réservé"
	}
	document.getElementById("id_nettoyage").onclick = function(){
		var prix = document.getElementById("prix").textContent;
		prix=prix*1
		var nettoyage = document.getElementById("nettoyage_donnée").textContent;
		nettoyage=nettoyage*1
		var afficher_prix = document.getElementById("info4");
		var a=document.getElementById("id_nettoyage").checked;
		if (a == true){
			afficher_prix.textContent="Prix total : " + prix + " € + " + nettoyage + " € de nettoyage = "+ (prix+nettoyage) + " €"
		}
		else
		{
			afficher_prix.textContent="Prix total : " + prix + " € + aucun nettoyage = "+ prix + " €"
		}
	}
	afficher_prix.textContent="Prix total : " + prix + " € + aucun nettoyage = "+ prix + " €"
}
