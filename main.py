def main():
    """
    ##################################################
    Comlete your code here
    Use m_perc and f_perc for your results
    ##################################################
    """
    Mnum = int(input('Enter number of Male students'))
    Fnum = int(input('Enter number of Female students')) 
    total = Fnum + Mnum 
    m_perc = Mnum / total * 100 
    f_perc = Fnum / total * 100 
    print (f'The percentage of the male students is {m_perc:.2f}')
    print (f'The percentage of the female students is {f_perc:.2f}')
    """
    ########################################
    # Do not delete the return statement
    ########################################
    """
    return m_perc, f_perc


if __name__ == '__main__':
    main()
