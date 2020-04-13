<?php
	system("gpio -g mode 12 out");
	system("gpio -g write 12 0");
	include "index.php"
?>
