import pandas as pd

def load_data():
    try:
        df = pd.read_csv("Day 4/imdb.csv")
        df.columns = df.columns.str.strip().str.lower()
        return df
    except FileNotFoundError:
        print("File not found. Please check your file path or name.")
        return None

def movie_reccomend(df):
    genre_input = input("Enter genre (e.g., Action, Comedy, Drama): ").strip().title()
    
    try:
        rating_input = float(input("Enter IMDb rating: ").strip())
    except ValueError:
        print("Invalid rating entered. Please enter a number.")
        return

    filtered_df = df[
        df['genre'].str.contains(genre_input, case=False, na=False) &
        (df['imdb_rating'] >= rating_input)
    ]   

    movies = filtered_df.sort_values(by='imdb_rating', ascending=False).head(5)

    if not movies.empty:
        print("\nTop Recommended Movies:")
        print(movies[['series_title', 'genre', 'imdb_rating']])  
    else:
        print("No movies found matching your criteria.")

if __name__ == "__main__":
    df = load_data()
    if df is not None:
        movie_reccomend(df)
