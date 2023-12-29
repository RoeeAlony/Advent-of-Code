using Day11;
using System;
using System.IO;
using System.Runtime.CompilerServices;



string path = "input.txt";
try
{
    List<Galaxy> galaxies = [];
    long rowOffset = 0;
    HashSet<int> colsWithGalaxies = []; 

    using StreamReader reader = new(path);
    string? line = reader.ReadLine() ?? throw new Exception();
    List<int> colOffset = [];
    int lineLength = line.Length;
    int rowIndex = 0;

    while (line != null)
    {
        bool isExpanding = true;
        for (int i=0; i<line.Length;i++)
        {
            if (line[i] == '#')
            {
                colsWithGalaxies.Add(i); 
                isExpanding = false;
                galaxies.Add(new Galaxy((Statics.Expantion * rowOffset)+rowIndex , i));
            }
        }

        if (isExpanding)
        {
            rowOffset++;
        }

        rowIndex++;
        line = reader.ReadLine();
    }

    foreach (int col in Enumerable.Range(0, lineLength)) {
        if (!colsWithGalaxies.Contains(col))
        {
            colOffset.Add(col);
        }
    }
    foreach(var col in colOffset) { Console.WriteLine("col offset: "+col); }

    long total = 0;
    for (int i=0; i<galaxies.Count-1;i++)
    {
        for (int j=i+1;j<galaxies.Count;j++)
        {
            total += galaxies[i].Compare(galaxies[j],colOffset);
        }
    }
    Console.WriteLine(total);
}
catch (IOException e)
{
    Console.WriteLine("An error occurred while reading the file.");
    Console.WriteLine(e.Message);
}



