namespace client
{
    partial class MainLayout
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
            this.exit_btn = new System.Windows.Forms.Button();
            this.label1 = new System.Windows.Forms.Label();
            this.referee_tb = new System.Windows.Forms.TextBox();
            this.label2 = new System.Windows.Forms.Label();
            this.game_tb = new System.Windows.Forms.TextBox();
            this.submit_btn = new System.Windows.Forms.Button();
            this.athlete_cb = new System.Windows.Forms.ComboBox();
            this.label3 = new System.Windows.Forms.Label();
            this.points_tb = new System.Windows.Forms.TextBox();
            this.label4 = new System.Windows.Forms.Label();
            this.label5 = new System.Windows.Forms.Label();
            this.totalPoints_lb = new System.Windows.Forms.ListBox();
            this.gameResults_lb = new System.Windows.Forms.ListBox();
            this.SuspendLayout();
            // 
            // exit_btn
            // 
            this.exit_btn.Location = new System.Drawing.Point(728, 12);
            this.exit_btn.Name = "exit_btn";
            this.exit_btn.Size = new System.Drawing.Size(37, 36);
            this.exit_btn.TabIndex = 0;
            this.exit_btn.Text = "X";
            this.exit_btn.UseVisualStyleBackColor = true;
            this.exit_btn.Click += new System.EventHandler(this.exit_btn_Click);
            // 
            // label1
            // 
            this.label1.Location = new System.Drawing.Point(29, 29);
            this.label1.Name = "label1";
            this.label1.Size = new System.Drawing.Size(59, 19);
            this.label1.TabIndex = 1;
            this.label1.Text = "Referee";
            // 
            // referee_tb
            // 
            this.referee_tb.Location = new System.Drawing.Point(94, 29);
            this.referee_tb.Name = "referee_tb";
            this.referee_tb.ReadOnly = true;
            this.referee_tb.Size = new System.Drawing.Size(218, 22);
            this.referee_tb.TabIndex = 2;
            // 
            // label2
            // 
            this.label2.Location = new System.Drawing.Point(361, 29);
            this.label2.Name = "label2";
            this.label2.Size = new System.Drawing.Size(50, 19);
            this.label2.TabIndex = 4;
            this.label2.Text = "Game";
            // 
            // game_tb
            // 
            this.game_tb.Location = new System.Drawing.Point(417, 26);
            this.game_tb.Name = "game_tb";
            this.game_tb.ReadOnly = true;
            this.game_tb.Size = new System.Drawing.Size(218, 22);
            this.game_tb.TabIndex = 5;
            // 
            // submit_btn
            // 
            this.submit_btn.Location = new System.Drawing.Point(673, 93);
            this.submit_btn.Name = "submit_btn";
            this.submit_btn.Size = new System.Drawing.Size(92, 45);
            this.submit_btn.TabIndex = 6;
            this.submit_btn.Text = "SUBMIT";
            this.submit_btn.UseVisualStyleBackColor = true;
            this.submit_btn.Click += new System.EventHandler(this.submit_btn_Click);
            // 
            // athlete_cb
            // 
            this.athlete_cb.FormattingEnabled = true;
            this.athlete_cb.Location = new System.Drawing.Point(351, 114);
            this.athlete_cb.Name = "athlete_cb";
            this.athlete_cb.Size = new System.Drawing.Size(121, 24);
            this.athlete_cb.TabIndex = 7;
            // 
            // label3
            // 
            this.label3.Location = new System.Drawing.Point(351, 92);
            this.label3.Name = "label3";
            this.label3.Size = new System.Drawing.Size(75, 19);
            this.label3.TabIndex = 8;
            this.label3.Text = "Athlete";
            // 
            // points_tb
            // 
            this.points_tb.Location = new System.Drawing.Point(514, 114);
            this.points_tb.Multiline = true;
            this.points_tb.Name = "points_tb";
            this.points_tb.Size = new System.Drawing.Size(121, 24);
            this.points_tb.TabIndex = 9;
            // 
            // label4
            // 
            this.label4.Location = new System.Drawing.Point(514, 92);
            this.label4.Name = "label4";
            this.label4.Size = new System.Drawing.Size(75, 19);
            this.label4.TabIndex = 10;
            this.label4.Text = "Points";
            // 
            // label5
            // 
            this.label5.Font = new System.Drawing.Font("Microsoft Sans Serif", 16.2F, System.Drawing.FontStyle.Bold, System.Drawing.GraphicsUnit.Point, ((byte) (0)));
            this.label5.Location = new System.Drawing.Point(50, 107);
            this.label5.Name = "label5";
            this.label5.Size = new System.Drawing.Size(230, 31);
            this.label5.TabIndex = 12;
            this.label5.Text = "TOTAL POINTS";
            // 
            // totalPoints_lb
            // 
            this.totalPoints_lb.FormattingEnabled = true;
            this.totalPoints_lb.ItemHeight = 16;
            this.totalPoints_lb.Location = new System.Drawing.Point(12, 157);
            this.totalPoints_lb.Name = "totalPoints_lb";
            this.totalPoints_lb.Size = new System.Drawing.Size(300, 276);
            this.totalPoints_lb.TabIndex = 13;
            // 
            // gameResults_lb
            // 
            this.gameResults_lb.FormattingEnabled = true;
            this.gameResults_lb.ItemHeight = 16;
            this.gameResults_lb.Location = new System.Drawing.Point(335, 157);
            this.gameResults_lb.Name = "gameResults_lb";
            this.gameResults_lb.Size = new System.Drawing.Size(430, 276);
            this.gameResults_lb.TabIndex = 14;
            // 
            // MainLayout
            // 
            this.AutoScaleDimensions = new System.Drawing.SizeF(8F, 16F);
            this.AutoScaleMode = System.Windows.Forms.AutoScaleMode.Font;
            this.ClientSize = new System.Drawing.Size(777, 443);
            this.Controls.Add(this.gameResults_lb);
            this.Controls.Add(this.totalPoints_lb);
            this.Controls.Add(this.label5);
            this.Controls.Add(this.label4);
            this.Controls.Add(this.points_tb);
            this.Controls.Add(this.label3);
            this.Controls.Add(this.athlete_cb);
            this.Controls.Add(this.submit_btn);
            this.Controls.Add(this.game_tb);
            this.Controls.Add(this.label2);
            this.Controls.Add(this.referee_tb);
            this.Controls.Add(this.label1);
            this.Controls.Add(this.exit_btn);
            this.Name = "MainLayout";
            this.Text = "MainLayout";
            this.ResumeLayout(false);
            this.PerformLayout();
        }

        private System.Windows.Forms.ListBox gameResults_lb;
        private System.Windows.Forms.ListBox totalPoints_lb;

        private System.Windows.Forms.Label label5;

        private System.Windows.Forms.Label label4;

        private System.Windows.Forms.TextBox points_tb;

        private System.Windows.Forms.ComboBox athlete_cb;
        private System.Windows.Forms.Label label3;

        private System.Windows.Forms.Button submit_btn;
        private System.Windows.Forms.TextBox game_tb;
        private System.Windows.Forms.Label label2;

        private System.Windows.Forms.Button exit_btn;
        private System.Windows.Forms.Label label1;
        private System.Windows.Forms.TextBox referee_tb;

        #endregion
    }
}