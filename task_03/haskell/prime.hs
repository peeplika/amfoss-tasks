import Control.Monad (forM_, when)

nestedForLoops :: Int -> IO ()
nestedForLoops rows = do
  forM_ [2 .. rows] $ \i -> do
    let isprime = all (\j -> i `mod` j /= 0) [2 .. i-1]
    when isprime $ putStrLn $ show i

main :: IO ()
main = do
  putStrLn "Enter an integer: "
  input <- getLine
  let number = read input :: Int
  if number <= 0
    then putStrLn "Not valid"
    else nestedForLoops number
  
