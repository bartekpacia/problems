import Foundation

let file = try! String(contentsOfFile: "sample.txt", encoding: .utf8).split(whereSeparator: \.isNewline)

for line in file {
    let parts = line.split(separator: ",")
    print("char: \(parts)")
    parts.split(separator: "-").map { $0 * 2 }

    //print("part1: \(parts[0]), part2: \(parts[1])")
}
