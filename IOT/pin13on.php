<?php
	system("gpio -g mode 13 out");
	system("gpio -g write 13 1");
	include "index.php"
?>
