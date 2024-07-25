using System;
using System.Collections.Generic;
using System.ComponentModel;
using System.Data;
using System.Drawing;
using System.Linq;
using System.Text;
using System.Threading.Tasks;
using System.Windows.Forms;

namespace Guia1
{
    public partial class Form1 : Form
    {
        public Form1()
        {
            InitializeComponent();
        }

        private void Form1_Load(object sender, EventArgs e)
        {

        }

        private void comboBox1_SelectedIndexChanged(object sender, EventArgs e)
        {

        }

        private void label1_Click(object sender, EventArgs e)
        {

        }

        private void button1_Click(object sender, EventArgs e)
        {
            int depto = this.comboBox1.SelectedIndex;
            double costo = Convert.ToDouble(this.numericUpDown1.Value);
            double precio = 0;
            if (depto == 0)
            {
                precio = costo * 0.90;
            }
            else if (depto == 1)
            {
                precio = costo * 0.95;
            }

            this.PrecioFinal.Text = precio.ToString();
        }
    }
}
