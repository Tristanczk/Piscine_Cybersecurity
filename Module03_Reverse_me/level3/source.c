# include <stdio.h>
# include <string.h>
# include <stdlib.h>

void	___syscall_malloc(void)
{
	puts("Nope.");
	exit(1);
}


void	____syscall_malloc(void)
{
	puts("Good job.");
	return;
}


int main(void)
{
	char	prop[31];
	char	key[9];
	char	cur_char[3];
	int		ret, i, j, len, value, check;

	printf("Please enter key: ");
	ret = scanf("%s", prop);
	if (ret != 1)
		___syscall_malloc();
	if (prop[1] != '2')
		___syscall_malloc();
	if (prop[0] != '4')
		___syscall_malloc();
	fflush(stdin);
	memset(key, 0, 9);
	key[0] = '*';
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
	check =  strcmp(key, "********");
	if (check == -2)
		___syscall_malloc();
	else if (check == -1)
		___syscall_malloc();
	else if (check == 0)
		____syscall_malloc();
	else if (check == 1)
		___syscall_malloc();
	else if (check == 2)
		___syscall_malloc();
	else if (check == 3)
		___syscall_malloc();
	else if (check == 4)
		___syscall_malloc();
	else if (check == 5)
		___syscall_malloc();
	else if (check == 115)
		___syscall_malloc();
	else
		___syscall_malloc();
	return 0;
}