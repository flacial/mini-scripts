import { pigLatin } from "../../text/pig-latin/pig-latin.ts";


describe('Pig Latin function', () => {
    it('Begins with Consonant: should return "ingstray" for string', () => {
        const result = pigLatin('string')
        expect(result).toEqual('ingstray');
    })

    it('Consonants Cluster: should return "ananabay" for banana', () => {
        const result = pigLatin('banana')
        expect(result).toEqual('ananabay');
    })

    it('Begins with Vowel: should return "eggay" for egg', () => {
        const result = pigLatin('egg')
        expect(result).toEqual('eggay');
    })

    it('should return "Please provide a word." for empty parameter', () => {
        const result = pigLatin()
        expect(result).toEqual('Please provide a word.');
    })
})