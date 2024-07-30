using System.Text.RegularExpressions;

const string PATH = @"Input.txt";
using var sr = new StreamReader(PATH);
string? line = sr.ReadLine() ?? throw new Exception();
int total = 0;
int i = 0;
Dictionary<int, int> CopiesDict = [];

while (line != null)
{
    HashSet<int> winningNumbers = [];
    HashSet<int> cardNumbers = [];
    var spliLine = line.Split('|');
    var line1 = spliLine[0];
    var line2 = spliLine[1];
    winningNumbers.UnionWith(Regex.Matches(line1, "\\d+").Skip(1)
        .Select(match => int.Parse(match.Value)));

    cardNumbers.UnionWith(Regex.Matches(line2, "\\d+")
        .Select(match => int.Parse(match.Value)));

    var matches = winningNumbers.Where(a => cardNumbers.Contains(a)).Count();

    CopiesDict[i] = CopiesDict.TryGetValue(i, out int value) ? value + 1 : 1;
    int multiplier= CopiesDict[i];    
    total += multiplier;

    if(matches>0)
        foreach (int match in Enumerable.Range(1, matches))
            CopiesDict[i + match] = CopiesDict.TryGetValue(i + match, out int valueOther) ? valueOther + 1*multiplier : 1*multiplier;

    line = sr.ReadLine();
    i++;
}
Console.WriteLine($"{total}");