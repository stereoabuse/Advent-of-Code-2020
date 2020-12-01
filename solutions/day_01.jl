
# Advent of Code 2020 Day 1

function part_1()
    lines = readlines(open("../inputs/01"))
    GOAL = 2020
    d = map(x->parse(Int64,x), lines)
    for a in d
        for b in d
            if a != b && a + b == GOAL
                return a * b
                break
            end
        end
    end
end


function part_2()
    lines = readlines(open("../inputs/01"))
    GOAL = 2020
    d = map(x->parse(Int64,x), lines)
    for a in d
        for b in d
            for c in d
                if a != b && b != c && a + b + c == GOAL
                    return a * b * c
                end
            end
        end
    end
end

print(part_1())
print(part_2())