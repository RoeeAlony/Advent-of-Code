const INPUT = "";

const gcd = (a: number, b: number): number => (b == 0 ? a : gcd(b, a % b));
const lcm = (a: number, b: number) => (a / gcd(a, b)) * b;
const lcmAll = (ns: number[]) => ns.reduce(lcm, 1);

type Direction = {
    str: string;
    location: string;
    right: string;
    left: string;
};


const sequence = INPUT.split("\n\n")[0];
const directionsStr = INPUT.split("\n\n")[1].replaceAll(" ", "").split("\n");

const directions: Direction[] = [];

for (const direction of directionsStr) {
    let [location, everythingElse] = direction.split("=");
    everythingElse = everythingElse.replaceAll("(", "").replaceAll(")", "");

    const [left, right] = everythingElse.split(",");

    directions.push({
        str: direction,
        left,
        right,
        location
    });
}

const start = directions.filter((dir) => dir.location.endsWith("A"))!;

let seqI = 0;
let currentPaths = start;
const steps: number[] = [];
for (const path of currentPaths) {
    seqI = 0;
    let currentPath = path;
    let currentSteps = 0;

    console.log(path);
    while (true) {
        currentPath =
            sequence[seqI] == "L"
                ? directions.find((dir) => dir.location == currentPath.left)!
                : directions.find((dir) => dir.location == currentPath.right)!;

        currentSteps++;

        if (currentPath.location.endsWith("Z")) break;

        seqI++;
        if (seqI >= sequence.length) seqI = 0;
    }

    steps.push(currentSteps);
}

console.log(lcmAll(steps));