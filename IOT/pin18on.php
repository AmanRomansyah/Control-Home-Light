<?php
	system("gpio -g mode 18 out");
	system("gpio -g write 18 1");
	include "index.php"
?>
