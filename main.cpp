int main() {
int x = n;
    unsigned int count = 1;
    while(x%2==0){
        x>>1;
        count++;
    }
    return count;
}