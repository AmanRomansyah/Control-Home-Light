<?php
	system("gpio -g mode 8 out");
	system("gpio -g write 8 0");
	include "index.php"
?>
