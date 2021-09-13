namespace lab1_tema
{
    partial class Form1
    {
        /// <summary>
        /// Required designer variable.
        /// </summary>
        private System.ComponentModel.IContainer components = null;

        /// <summary>
        /// Clean up any resources being used.
        /// </summary>
        /// <param name="disposing">true if managed resources should be disposed; otherwise, false.</param>
        protected override void Dispose(bool disposing)
        {
            if (disposing && (components != null))
            {
                components.Dispose();
            }
            base.Dispose(disposing);
        }

        #region Windows Form Designer generated code

        /// <summary>
        /// Required method for Designer support - do not modify
        /// the contents of this method with the code editor.
        /// </summary>
        private void InitializeComponent()
        {
            System.Windows.Forms.DataGridViewCellStyle dataGridViewCellStyle3 = new System.Windows.Forms.DataGridViewCellStyle();
            System.Windows.Forms.DataGridViewCellStyle dataGridViewCellStyle4 = new System.Windows.Forms.DataGridViewCellStyle();
            this.dgvCities = new System.Windows.Forms.DataGridView();
            this.label1 = new System.Windows.Forms.Label();
            this.dgvShops = new System.Windows.Forms.DataGridView();
            this.label2 = new System.Windows.Forms.Label();
            this.deleteShopBtn = new System.Windows.Forms.Button();
            this.updateShooBtn = new System.Windows.Forms.Button();
            this.label3 = new System.Windows.Forms.Label();
            this.label4 = new System.Windows.Forms.Label();
            this.label5 = new System.Windows.Forms.Label();
            this.label6 = new System.Windows.Forms.Label();
            this.locationTb = new System.Windows.Forms.TextBox();
            this.cityIdCb = new System.Windows.Forms.ComboBox();
            this.openHourNumeric = new System.Windows.Forms.NumericUpDown();
            this.closeHourNumeric = new System.Windows.Forms.NumericUpDown();
            this.addBtn = new System.Windows.Forms.Button();
            this.resetBtn = new System.Windows.Forms.Button();
            ((System.ComponentModel.ISupportInitialize)(this.dgvCities)).BeginInit();
            ((System.ComponentModel.ISupportInitialize)(this.dgvShops)).BeginInit();
            ((System.ComponentModel.ISupportInitialize)(this.openHourNumeric)).BeginInit();
            ((System.ComponentModel.ISupportInitialize)(this.closeHourNumeric)).BeginInit();
            this.SuspendLayout();
            // 
            // dgvCities
            // 
            this.dgvCities.BorderStyle = System.Windows.Forms.BorderStyle.Fixed3D;
            this.dgvCities.ColumnHeadersHeightSizeMode = System.Windows.Forms.DataGridViewColumnHeadersHeightSizeMode.AutoSize;
            dataGridViewCellStyle3.Alignment = System.Windows.Forms.DataGridViewContentAlignment.MiddleLeft;
            dataGridViewCellStyle3.BackColor = System.Drawing.SystemColors.Window;
            dataGridViewCellStyle3.Font = new System.Drawing.Font("Microsoft Sans Serif", 7.8F, System.Drawing.FontStyle.Regular, System.Drawing.GraphicsUnit.Point, ((byte)(0)));
            dataGridViewCellStyle3.ForeColor = System.Drawing.SystemColors.ControlText;
            dataGridViewCellStyle3.SelectionBackColor = System.Drawing.Color.FromArgb(((int)(((byte)(255)))), ((int)(((byte)(128)))), ((int)(((byte)(0)))));
            dataGridViewCellStyle3.SelectionForeColor = System.Drawing.SystemColors.HighlightText;
            dataGridViewCellStyle3.WrapMode = System.Windows.Forms.DataGridViewTriState.False;
            this.dgvCities.DefaultCellStyle = dataGridViewCellStyle3;
            this.dgvCities.Location = new System.Drawing.Point(74, 111);
            this.dgvCities.Name = "dgvCities";
            this.dgvCities.ReadOnly = true;
            this.dgvCities.RowHeadersWidth = 51;
            this.dgvCities.RowTemplate.Height = 24;
            this.dgvCities.SelectionMode = System.Windows.Forms.DataGridViewSelectionMode.FullRowSelect;
            this.dgvCities.Size = new System.Drawing.Size(368, 390);
            this.dgvCities.TabIndex = 0;
            this.dgvCities.CellMouseClick += new System.Windows.Forms.DataGridViewCellMouseEventHandler(this.dgvCities_CellMouseClick);
            // 
            // label1
            // 
            this.label1.AutoSize = true;
            this.label1.Font = new System.Drawing.Font("Microsoft Sans Serif", 13.8F, System.Drawing.FontStyle.Bold, System.Drawing.GraphicsUnit.Point, ((byte)(0)));
            this.label1.Location = new System.Drawing.Point(132, 68);
            this.label1.Name = "label1";
            this.label1.Size = new System.Drawing.Size(244, 29);
            this.label1.TabIndex = 1;
            this.label1.Text = "Cities (parent table)";
            // 
            // dgvShops
            // 
            this.dgvShops.BorderStyle = System.Windows.Forms.BorderStyle.Fixed3D;
            this.dgvShops.ColumnHeadersHeightSizeMode = System.Windows.Forms.DataGridViewColumnHeadersHeightSizeMode.AutoSize;
            dataGridViewCellStyle4.Alignment = System.Windows.Forms.DataGridViewContentAlignment.MiddleLeft;
            dataGridViewCellStyle4.BackColor = System.Drawing.SystemColors.Window;
            dataGridViewCellStyle4.Font = new System.Drawing.Font("Microsoft Sans Serif", 7.8F, System.Drawing.FontStyle.Regular, System.Drawing.GraphicsUnit.Point, ((byte)(0)));
            dataGridViewCellStyle4.ForeColor = System.Drawing.SystemColors.ControlText;
            dataGridViewCellStyle4.SelectionBackColor = System.Drawing.Color.FromArgb(((int)(((byte)(255)))), ((int)(((byte)(128)))), ((int)(((byte)(0)))));
            dataGridViewCellStyle4.SelectionForeColor = System.Drawing.SystemColors.HighlightText;
            dataGridViewCellStyle4.WrapMode = System.Windows.Forms.DataGridViewTriState.False;
            this.dgvShops.DefaultCellStyle = dataGridViewCellStyle4;
            this.dgvShops.EditMode = System.Windows.Forms.DataGridViewEditMode.EditProgrammatically;
            this.dgvShops.Location = new System.Drawing.Point(712, 111);
            this.dgvShops.Name = "dgvShops";
            this.dgvShops.RowHeadersWidth = 51;
            this.dgvShops.RowTemplate.Height = 24;
            this.dgvShops.SelectionMode = System.Windows.Forms.DataGridViewSelectionMode.FullRowSelect;
            this.dgvShops.Size = new System.Drawing.Size(355, 390);
            this.dgvShops.TabIndex = 2;
            // 
            // label2
            // 
            this.label2.AutoSize = true;
            this.label2.Font = new System.Drawing.Font("Microsoft Sans Serif", 13.8F, System.Drawing.FontStyle.Bold, System.Drawing.GraphicsUnit.Point, ((byte)(0)));
            this.label2.Location = new System.Drawing.Point(774, 68);
            this.label2.Name = "label2";
            this.label2.Size = new System.Drawing.Size(233, 29);
            this.label2.TabIndex = 3;
            this.label2.Text = "Shops (child table)";
            // 
            // deleteShopBtn
            // 
            this.deleteShopBtn.Location = new System.Drawing.Point(507, 411);
            this.deleteShopBtn.Name = "deleteShopBtn";
            this.deleteShopBtn.Size = new System.Drawing.Size(138, 36);
            this.deleteShopBtn.TabIndex = 4;
            this.deleteShopBtn.Text = "DELETE";
            this.deleteShopBtn.UseVisualStyleBackColor = true;
            this.deleteShopBtn.Click += new System.EventHandler(this.deleteShopBtn_Click);
            // 
            // updateShooBtn
            // 
            this.updateShooBtn.Location = new System.Drawing.Point(507, 359);
            this.updateShooBtn.Name = "updateShooBtn";
            this.updateShooBtn.Size = new System.Drawing.Size(138, 36);
            this.updateShooBtn.TabIndex = 5;
            this.updateShooBtn.Text = "UPDATE";
            this.updateShooBtn.UseVisualStyleBackColor = true;
            this.updateShooBtn.Click += new System.EventHandler(this.updateShooBtn_Click);
            // 
            // label3
            // 
            this.label3.AutoSize = true;
            this.label3.Location = new System.Drawing.Point(476, 45);
            this.label3.Name = "label3";
            this.label3.Size = new System.Drawing.Size(78, 17);
            this.label3.TabIndex = 6;
            this.label3.Text = "LOCATION";
            // 
            // label4
            // 
            this.label4.AutoSize = true;
            this.label4.Location = new System.Drawing.Point(476, 105);
            this.label4.Name = "label4";
            this.label4.Size = new System.Drawing.Size(92, 17);
            this.label4.TabIndex = 7;
            this.label4.Text = "OPEN HOUR";
            // 
            // label5
            // 
            this.label5.AutoSize = true;
            this.label5.Location = new System.Drawing.Point(476, 162);
            this.label5.Name = "label5";
            this.label5.Size = new System.Drawing.Size(99, 17);
            this.label5.TabIndex = 8;
            this.label5.Text = "CLOSE HOUR";
            // 
            // label6
            // 
            this.label6.AutoSize = true;
            this.label6.Location = new System.Drawing.Point(476, 223);
            this.label6.Name = "label6";
            this.label6.Size = new System.Drawing.Size(55, 17);
            this.label6.TabIndex = 9;
            this.label6.Text = "CITY ID";
            this.label6.Click += new System.EventHandler(this.label6_Click);
            // 
            // locationTb
            // 
            this.locationTb.Location = new System.Drawing.Point(479, 65);
            this.locationTb.Name = "locationTb";
            this.locationTb.Size = new System.Drawing.Size(192, 22);
            this.locationTb.TabIndex = 10;
            this.locationTb.TextChanged += new System.EventHandler(this.textBox1_TextChanged);
            // 
            // cityIdCb
            // 
            this.cityIdCb.FormattingEnabled = true;
            this.cityIdCb.Location = new System.Drawing.Point(479, 243);
            this.cityIdCb.Name = "cityIdCb";
            this.cityIdCb.Size = new System.Drawing.Size(192, 24);
            this.cityIdCb.TabIndex = 13;
            // 
            // openHourNumeric
            // 
            this.openHourNumeric.Location = new System.Drawing.Point(479, 126);
            this.openHourNumeric.Name = "openHourNumeric";
            this.openHourNumeric.Size = new System.Drawing.Size(192, 22);
            this.openHourNumeric.TabIndex = 14;
            // 
            // closeHourNumeric
            // 
            this.closeHourNumeric.Location = new System.Drawing.Point(479, 183);
            this.closeHourNumeric.Maximum = new decimal(new int[] {
            23,
            0,
            0,
            0});
            this.closeHourNumeric.Name = "closeHourNumeric";
            this.closeHourNumeric.Size = new System.Drawing.Size(192, 22);
            this.closeHourNumeric.TabIndex = 15;
            // 
            // addBtn
            // 
            this.addBtn.Location = new System.Drawing.Point(507, 301);
            this.addBtn.Name = "addBtn";
            this.addBtn.Size = new System.Drawing.Size(138, 39);
            this.addBtn.TabIndex = 16;
            this.addBtn.Text = "ADD";
            this.addBtn.UseVisualStyleBackColor = true;
            this.addBtn.Click += new System.EventHandler(this.button1_Click);
            // 
            // resetBtn
            // 
            this.resetBtn.Location = new System.Drawing.Point(507, 465);
            this.resetBtn.Name = "resetBtn";
            this.resetBtn.Size = new System.Drawing.Size(138, 36);
            this.resetBtn.TabIndex = 17;
            this.resetBtn.Text = "RESET";
            this.resetBtn.UseVisualStyleBackColor = true;
            this.resetBtn.Click += new System.EventHandler(this.resetBtn_Click);
            // 
            // Form1
            // 
            this.AutoScaleDimensions = new System.Drawing.SizeF(8F, 16F);
            this.AutoScaleMode = System.Windows.Forms.AutoScaleMode.Font;
            this.ClientSize = new System.Drawing.Size(1151, 541);
            this.Controls.Add(this.resetBtn);
            this.Controls.Add(this.addBtn);
            this.Controls.Add(this.closeHourNumeric);
            this.Controls.Add(this.openHourNumeric);
            this.Controls.Add(this.cityIdCb);
            this.Controls.Add(this.locationTb);
            this.Controls.Add(this.label6);
            this.Controls.Add(this.label5);
            this.Controls.Add(this.label4);
            this.Controls.Add(this.label3);
            this.Controls.Add(this.updateShooBtn);
            this.Controls.Add(this.deleteShopBtn);
            this.Controls.Add(this.label2);
            this.Controls.Add(this.dgvShops);
            this.Controls.Add(this.label1);
            this.Controls.Add(this.dgvCities);
            this.Name = "Form1";
            this.Text = "Form1";
            this.Load += new System.EventHandler(this.Form1_Load);
            ((System.ComponentModel.ISupportInitialize)(this.dgvCities)).EndInit();
            ((System.ComponentModel.ISupportInitialize)(this.dgvShops)).EndInit();
            ((System.ComponentModel.ISupportInitialize)(this.openHourNumeric)).EndInit();
            ((System.ComponentModel.ISupportInitialize)(this.closeHourNumeric)).EndInit();
            this.ResumeLayout(false);
            this.PerformLayout();

        }

        #endregion

        private System.Windows.Forms.DataGridView dgvCities;
        private System.Windows.Forms.Label label1;
        private System.Windows.Forms.DataGridView dgvShops;
        private System.Windows.Forms.Label label2;
        private System.Windows.Forms.Button deleteShopBtn;
        private System.Windows.Forms.Button updateShooBtn;
        private System.Windows.Forms.Label label3;
        private System.Windows.Forms.Label label4;
        private System.Windows.Forms.Label label5;
        private System.Windows.Forms.Label label6;
        private System.Windows.Forms.TextBox locationTb;
        private System.Windows.Forms.ComboBox cityIdCb;
        private System.Windows.Forms.NumericUpDown openHourNumeric;
        private System.Windows.Forms.NumericUpDown closeHourNumeric;
        private System.Windows.Forms.Button addBtn;
        private System.Windows.Forms.Button resetBtn;
    }
}

