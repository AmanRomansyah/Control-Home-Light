<?php
	system("gpio -g mode 16 out");
	system("gpio -g write 16 0");
	include "index.php"
?>
