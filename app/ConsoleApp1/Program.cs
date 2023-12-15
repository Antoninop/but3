using System;
using System.Collections.Generic;
using System.IO;
using System.Globalization;

struct Etudiant
{
    public string Nom;
    public string Prenom;
    public List<float> Notes;
}

class Program
{
    static void Main()
    {
        string cheminFichierCSV = "../../../../bdd.csv";
        List<string> prenomsEtudiants = new List<string>();
        List<string> nomsEtudiants = new List<string>();
        List<List<float>> notesEtudiants = new List<List<float>>();

        try
        {
            string[] lignes = File.ReadAllLines(cheminFichierCSV);

            // passe la ligne entête
            bool premiereLigne = true;

            foreach (var ligne in lignes)
            {
                if (premiereLigne)
                {
                    premiereLigne = false;
                    continue;
                }

                string[] colonnes = ligne.Split(';');

                Etudiant etudiant = new Etudiant();

                etudiant.Nom = colonnes[5];
                etudiant.Prenom = colonnes[6];
                etudiant.Notes = new List<float>();

                for (int i = 0; i < 3; i++)
                {
                    // Vérifiez si la note est présente et n'est pas une chaîne vide
                    if (!string.IsNullOrWhiteSpace(colonnes[14 + i]))
                    {
                        // Convertissez la chaîne en float
                        float note;
                        if (float.TryParse(colonnes[14 + i].Replace(',', '.'), NumberStyles.Float, CultureInfo.InvariantCulture, out note))
                        {
                            etudiant.Notes.Add(note);
                        }
                        else
                        {
                            // Gestion des cas où la conversion échoue
                            Console.WriteLine($"Erreur de conversion de la note à la colonne {14 + i} pour l'étudiant {etudiant.Nom} {etudiant.Prenom}");
                        }
                    }
                }

                nomsEtudiants.Add(etudiant.Nom);
                prenomsEtudiants.Add(etudiant.Prenom);
                notesEtudiants.Add(etudiant.Notes);
            }

            Console.WriteLine("Etudiants:");
            Console.WriteLine();

            for (int i = 0; i < prenomsEtudiants.Count; i++)
            {
                Console.WriteLine("Nom: " + nomsEtudiants[i]);
                Console.WriteLine("Prenom: " + prenomsEtudiants[i]);
                Console.WriteLine("Notes: " + string.Join(", ", notesEtudiants[i].Select(n => n.ToString("F2"))));
                Console.WriteLine();
            }
        }
        catch (Exception ex)
        {
            Console.WriteLine($"Une erreur s'est produite : {ex.Message}");
        }

        Console.ReadLine();
    }
}
