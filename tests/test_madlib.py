from madlib_cli_1.madlib import read_file ,parse ,merge_and_write_file

def test_read() :
    
    expected = open('assets/mad_file.txt').read().strip()
    received = read_file()
    assert expected == received

def user_input_test () : 
    accepted =  'please  enter name  >> '
    actual = user_input(['name'])
    assert accepted == actual

def test_Parse():
    expected = ["majd","27"]
    received = parse( "hello i ma {majd}, I am {27} years old")
    assert expected == received

def testMerge():
    words = ['smart', 'boxes', 'hungry', 'eat']
    text = 'A {} {} had a {} dog so they {} them'
    received = merge_and_write_file(words, text)
    expected = 'A smart boxes had a hungry dog so they eat them'
    assert expected == received

