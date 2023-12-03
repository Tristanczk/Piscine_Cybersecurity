# include <stdio.h>
# include <string.h>
# include <stdlib.h>

void	no(void)
{
	puts("Nope.");
	exit(1);
}


void	ok(void)
{
	puts("Good job.");
	return;
}


int main(void)
{
	char	prop[24];
	char	key[9];
	char	cur_char[3];
	int		ret, i, j, len, value;

	printf("Please enter key: ");
	ret = scanf("%s", prop);
	if (ret != 1)
		no();
	if (prop[1] != '0')
		no();
	if (prop[0] != '0')
		no();
	fflush(stdin);
	memset(key, 0, 9);
	key[0] = 'd';
	i = 2;
	j = 1;
	while (1)
	{
		len = strlen(key);
		if (len < 8) {
			len = strlen(prop);
		}
		else
			break;
		if (i >= len)
			break;
		cur_char[0] = prop[i];
		cur_char[1] = prop[i + 1];
		cur_char[2] = prop[i + 2];
		value = atoi(cur_char);
		key[j] = (char) value;
		i += 3;
		j += 1;
	}
	key[j] = '\0';
	if (strcmp(key, "delabere") == 0)
		ok();
	else
		no();
	return 0;
}