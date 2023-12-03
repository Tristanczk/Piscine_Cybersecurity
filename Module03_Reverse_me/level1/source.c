# include <stdio.h>
# include <string.h>

int main(void)
{
	char to_compare[100];
	printf("Please enter key: ");
	scanf("%s", to_compare);
	if (strcmp(to_compare, "__stack_check") == 0)
		printf("Good job.\n");
	else
		printf("Nope.\n");
}
