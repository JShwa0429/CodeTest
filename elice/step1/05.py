def main():
    chicken = {"count" : 0, "gram" : 40}
    peanut = {"count" : 0, "gram" : 10}
    pure = {"count" : 0, "gram" : 250}

    gram = int(input())
    remainder = 0

    pure["count"] = gram // pure["gram"]
    remainder = gram % pure["gram"]

    chicken["count"] = remainder // chicken["gram"]
    remainder = remainder % chicken["gram"]

    peanut["count"] = remainder // peanut["gram"]
    remainder = remainder % peanut["gram"]
    
    if remainder != 0:
        print(-1)
        return

    print(peanut["count"],chicken["count"],pure["count"],sep=" ");
if __name__ == "__main__":
    main()