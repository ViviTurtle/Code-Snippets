from classes import *
"""Used as Proof-of-Concept to show that private classes are not imported with wildcard imports"""

if __name__ == "__main__":

    public = Public("apple")
    public.public_class()
    public._private_class()

    #This Main Method should break here since Private was not imported due to wild card restraints
    private = _Private("apple")

    private_test.public_class()
    private_test._private_class()

