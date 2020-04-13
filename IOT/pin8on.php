<?php
	system("gpio -g mode 8 out");
	system("gpio -g write 8 1");
	include "index.php"
?>
