bool checkBit(int a, int n)
{
    return ((a >> n) & 0x1) == 1;
}

bool checkByte(int a)
{
    return checkBit(a, 7) && !checkBit(a, 6);
}

bool validUtf8(int* data, int dataSize) {
    if(dataSize < 0)
        return false;
    else if(dataSize == 0)
        return true;
        
    int a = data[0];
    if(!checkBit(a, 7))
    {
        if(validUtf8(data + 1, dataSize - 1))
            return true;
        else
        {
            printf("1\n");
            return false;
        }
    }
    else if(!checkBit(a, 6))
    {
        printf("2\n");
        return false;
    }
    else if(!checkBit(a, 5))
    {
        if(checkByte(data[1]) && validUtf8(data + 2, dataSize - 2))
            return true;
        else
        {
            printf("3\n");
            return false;
        }
    }
    else if(!checkBit(a, 4))
    {
        if(checkByte(data[1]) && checkByte(data[2]) && validUtf8(data + 3, dataSize - 3))
            return true;
        else
        {
            printf("4\n");
            return false;
        }
    }
    else if(!checkBit(a, 3))
    {
        if(checkByte(data[1]) && checkByte(data[2]) && checkByte(data[3]) && validUtf8(data + 4, dataSize - 4))
            return true;
        else
        {
            printf("5\n");
            return false;
        }
    }
    else
    {
        printf("6\n");
        return false;
    }
}