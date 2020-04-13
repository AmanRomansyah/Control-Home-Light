<?php
	system("gpio -g mode 5 out");
	system("gpio -g mode 7 out");
	system("gpio -g mode 8 out");
	system("gpio -g mode 12 out");
	system("gpio -g mode 13 out");
	system("gpio -g mode 16 out");
	system("gpio -g mode 17 out");
	system("gpio -g mode 18 out");
	system("gpio -g mode 19 out");
	system("gpio -g mode 20 out");
		
	system("gpio -g write 5 1");
	system("gpio -g write 7 1");
	system("gpio -g write 8 1");
	system("gpio -g write 12 1");
	system("gpio -g write 13 1");
	system("gpio -g write 16 1");
	system("gpio -g write 17 1");
	system("gpio -g write 18 1");
	system("gpio -g write 19 1");
	system("gpio -g write 20 1");
	
	include "index.php"
?>
