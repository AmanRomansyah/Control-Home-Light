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
	
	system("gpio -g write 5 0");
	system("gpio -g write 7 0");
	system("gpio -g write 8 0");
	system("gpio -g write 12 0");
	system("gpio -g write 13 0");
	system("gpio -g write 16 0");
	system("gpio -g write 17 0");
	system("gpio -g write 18 0");
	system("gpio -g write 19 0");
	system("gpio -g write 20 0");
	
	include "index.php"
?>
