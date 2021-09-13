using System;
using System.Data;
using System.Data.SqlClient;
using System.Windows.Forms;

namespace lab1_tema
{
    public partial class Form1 : Form
    {
        static SqlConnection conn = null;
        public Form1()
        {
            InitializeComponent();
            LoadParent();
            dgvCities.SelectionChanged += LoadChild;
            dgvShops.SelectionChanged += HandleEditing;
        }

        private static SqlConnection GetConnection()
        {
            if (conn == null)
            {
                conn = new SqlConnection("Server=DESKTOP-LLHQVU9;Database=L1;Integrated Security=true;");
            }
            if (conn.State == ConnectionState.Closed)
            {
                conn.Open();
            }
            return conn;
        }
        private void LoadParent()
        {
            using (SqlCommand cmd = new SqlCommand("select * from CITY", GetConnection()))
            {
                try
                {
                    SqlDataAdapter cityDA = new SqlDataAdapter(cmd);
                    DataSet cityDS = new DataSet();
                    cityDA.Fill(cityDS, "CITIES");
                    dgvCities.DataSource = cityDS.Tables["CITIES"];
                }
                catch (Exception ex)
                {
                    MessageBox.Show(ex.Message);
                }
            }
        }
        private void LoadChild(object sender, EventArgs e)
        {
            LoadChild();
        }
        private void LoadChild()
        {
            using (SqlCommand cmd = new SqlCommand("select * from SHOP where ID_CITY=@id", GetConnection()))
            {
                try
                {
                    int id = Convert.ToInt32(dgvCities.CurrentRow.Cells[0].Value);
                    cmd.Parameters.AddWithValue("@id", id);
                    SqlDataAdapter shopDA = new SqlDataAdapter(cmd);
                    DataSet shopDS = new DataSet();
                    shopDA.Fill(shopDS, "SHOPS");
                    dgvShops.DataSource = shopDS.Tables["SHOPS"];
                }
                catch (Exception ex)
                {
                    MessageBox.Show(ex.Message);
                }
            }
        }
        private void HandleEditing(object sender, EventArgs e)
        {
            HandleEditing();
        }
        private void HandleEditing()
        {
            using (SqlCommand cmd = new SqlCommand("select ID from SHOP", GetConnection()))
            {
                try
                {
                    if (dgvShops.SelectedRows.Count > 0)
                    {
                        int selectedrowindex = dgvShops.SelectedRows[0].Index;
                        if (selectedrowindex == dgvShops.Rows.Count - 1)
                        {
                            deleteShopBtn.Enabled = false;
                            updateShooBtn.Enabled = false;
                            return;
                        }
                        var selectedRow = dgvShops.Rows[selectedrowindex];
                        locationTb.Text = Convert.ToString(selectedRow.Cells["LOCATION"].Value);
                        openHourNumeric.Value = Convert.ToInt32(selectedRow.Cells["OPEN_HOUR"].Value);
                        closeHourNumeric.Value = Convert.ToInt32(selectedRow.Cells["CLOSE_HOUR"].Value);
                        cityIdCb.SelectedValue = Convert.ToInt32(selectedRow.Cells["ID_CITY"].Value);
                    }
                }
                catch (Exception ex)
                {
                    MessageBox.Show(ex.Message);
                }
            }
            deleteShopBtn.Enabled = true;
            updateShooBtn.Enabled = true;
        }
        private void PopulateCityIds()
        {
            using (SqlCommand cmd = new SqlCommand("select ID from CITY", GetConnection()))
            {
                try
                {
                    SqlDataAdapter cityDA = new SqlDataAdapter(cmd);
                    DataSet cityDS = new DataSet();
                    cityDA.Fill(cityDS, "ID");
                    cityIdCb.ValueMember = "ID";
                    cityIdCb.DataSource = cityDS.Tables["ID"];
                }
                catch (Exception ex)
                {
                    MessageBox.Show(ex.Message);
                }
            }
        }
        private void Form1_Load(object sender, EventArgs e)
        {
            this.Text = "Lant de magazine";
            DisableShopButtons();
            PopulateCityIds();
        }

        private void deleteShopBtn_Click(object sender, EventArgs e)
        {
            using (SqlCommand cmd = new SqlCommand("delete from SHOP where ID=@id", GetConnection()))
            {
                try
                {
                    int selectedChildId = Convert.ToInt32(dgvShops.CurrentRow.Cells[0].Value);

                    cmd.Parameters.AddWithValue("@id", selectedChildId);
                    cmd.ExecuteNonQuery();

                    LoadChild();
                    DisableShopButtons();
                    MessageBox.Show("Stergere realizata cu succes");
                }
                catch (Exception ex)
                {
                    MessageBox.Show(ex.Message);
                }
            }
        }

        private void label6_Click(object sender, EventArgs e)
        {

        }

        private void textBox1_TextChanged(object sender, EventArgs e)
        {

        }

        private void dgvCities_CellMouseClick(object sender, DataGridViewCellMouseEventArgs e)
        {
            DisableShopButtons();
        }

        private void updateShooBtn_Click(object sender, EventArgs e)
        {
            string commandString = "update SHOP set LOCATION=@location, OPEN_HOUR=@open, CLOSE_HOUR=@close, ID_CITY=@cityId where ID=@id";
            using (SqlCommand cmd = new SqlCommand(commandString, GetConnection()))
            {
                try
                {
                    int selectedChildId = Convert.ToInt32(dgvShops.CurrentRow.Cells[0].Value);

                    cmd.Parameters.AddWithValue("@location", locationTb.Text);
                    cmd.Parameters.AddWithValue("@open", openHourNumeric.Value);
                    cmd.Parameters.AddWithValue("@close", closeHourNumeric.Value);
                    cmd.Parameters.AddWithValue("@cityId", cityIdCb.Text);
                    cmd.Parameters.AddWithValue("@id", selectedChildId);
                    cmd.ExecuteNonQuery();

                    LoadChild();
                    DisableShopButtons();
                    MessageBox.Show("Modificare realizata cu succes");
                }
                catch (Exception ex)
                {
                    MessageBox.Show(ex.Message);
                }
            }
        }
        private void DisableShopButtons()
        {
            if (dgvShops.SelectedRows.Count < 1 || dgvShops.SelectedRows[0].Index == dgvShops.Rows.Count - 1)
            {
                deleteShopBtn.Enabled = false;
                updateShooBtn.Enabled = false;
            }
        }

        private void resetBtn_Click(object sender, EventArgs e)
        {
            locationTb.Text = "";
            openHourNumeric.Value = 0;
            closeHourNumeric.Value = 0;
            cityIdCb.SelectedIndex = 0;
        }

        private void button1_Click(object sender, EventArgs e)
        {
            string commandString = "insert into SHOP(LOCATION, OPEN_HOUR, CLOSE_HOUR, ID_CITY) values(@location, @open, @close, @cityId)";
            using (SqlCommand cmd = new SqlCommand(commandString, GetConnection()))
            {
                try
                {
                    cmd.Parameters.AddWithValue("@location", locationTb.Text);
                    cmd.Parameters.AddWithValue("@open", openHourNumeric.Value);
                    cmd.Parameters.AddWithValue("@close", closeHourNumeric.Value);
                    cmd.Parameters.AddWithValue("@cityId", Convert.ToInt32(dgvCities.CurrentRow.Cells["ID"].Value));
                    cmd.ExecuteNonQuery();

                    LoadChild();
                    DisableShopButtons();
                    MessageBox.Show("Modificare realizata cu succes");
                }
                catch (Exception ex)
                {
                    MessageBox.Show(ex.Message);
                }
            }
        }
    }
}
