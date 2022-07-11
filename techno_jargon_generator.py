import random

#defining possible words for doodoo poopoo caca code

dic1 = {"a": "Amplifying" , "b": "Badgering" , "c": "Calculating" , "d": "Drifting" , "e": "Energizing" , "f": "Foreseeing" , 
        "g": "Gerrymandering" , "h": "Hamstringing" , "i": "Inscribing" , "k": "Keelhauling" , "l": "Lemniscating" , "m": "Multiprogramming" , 
        "n": "Nesting" , "o": "Outlawing" , "p": "Perusing" , "r": "Reticulating" ,"s": "Sublimating" , "t": "Tobboganning" , 
        "u": "Unraveling" , "v": "Verifying" , "w": "Winding" , "x": "Xeroprinting"}

dic2 = {"a": "absurdities" , "b": "balletomanes" , "c": "calculations" , "d": "dauphins" , "e": "easements" , "f": "fakers" , 
        "g": "galvanisms" , "h": "happenstances" , "i": "iconoclasms" , "k": "kernels" , "l": "lagoons" , "m": "maelstroms" , 
        "n": "nebulas" , "o": "obelisks" , "p": "packets" , "r": "radiocarbons" , "s": "scaffolding" , "t": "textures" , 
        "u": "undercurrents" , "v": "valves" , "w": "warnings"}

letters = [ "a", "b", "c", "d", "e", "f", "g", "h", "i", "k", "l", 
            "m", "n", "o", "p", "r", "s", "t", "u", "v", "w"]

def jargon():
    l1 = random.choice(letters)
    l2 = random.choice(letters)
    word1 = dic1.get(str(l1), 0)
    word2 = dic2.get(str(l2), 0) 
    print(str(word1) + " " + str(word2))