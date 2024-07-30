using System.Runtime.CompilerServices;
using System.Text.RegularExpressions;

const string PATH = @"Input.txt";
using var sr = new StreamReader(PATH);
string? line = sr.ReadLine() ?? throw new Exception();

double sum = 0;
while (line != null)
{
    HashSet<int> winningNumbers = [];
    HashSet<int> cardNumbers = [];
    var spliLine = line.Split('|');
    var line1 = spliLine[0];
    var line2 = spliLine[1];
    winningNumbers.UnionWith(Regex.Matches(line1,"\\d+").Skip(1)
        .Select(match=>int.Parse(match.Value)));

    cardNumbers.UnionWith(Regex.Matches(line2, "\\d+")
        .Select(match => int.Parse(match.Value)));

    var matches = winningNumbers.Where(a => cardNumbers.Contains(a)).Count();
    sum += matches>0? Math.Pow(2,matches-1) : 0;

    line = sr.ReadLine();
}
    Console.WriteLine($"{sum}");