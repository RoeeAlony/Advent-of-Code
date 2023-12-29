using System;
using System.Collections.Generic;
using System.Linq;
using System.Text;
using System.Threading.Tasks;

namespace Day11
{
    static class Statics { 
    public static int  Expantion { get; set; } = 1; 
    }


    public class Galaxy(long row, long col)
    {
        public bool IsColOffset { get; set; } = false;
        public long Row { get; set; } = row;
        public long Col { get; set; } = col;

        public void AddColOffset(ICollection<int> offsetlist)
        {
            int offset = 0;
            foreach (int i in offsetlist)
                if (i < Col) offset++;
                else break;
            this.Col += offset* Statics.Expantion ;
            this.IsColOffset = true;
        }

        public long Compare(Galaxy other, ICollection<int> offsetlist)
        {
            if (!IsColOffset)
                AddColOffset(offsetlist);
            if (!other.IsColOffset)
                other.AddColOffset(offsetlist);

            return
            Math.Abs(this.Row - other.Row) +
            Math.Abs((this.Col - other.Col));
        }
    }
}
