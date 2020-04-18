#include <iostream>
#include <fstream>
#include <sstream>
#include <string>
#include <vector>
#include <map> 
#include <utility>
#include <chrono>
#include <algorithm>
#include <iterator>
#include <set>

using namespace std;

int K = 0;
int N = 0;
int M = 0;
int size_sol = 0;
bool has_value = false;
bool is_displayed = false;

vector<vector<int>> matrix;
set<int> infected_persons;
map<int, pair<string, pair<set<int>, set<int>>>> persons_map;
vector <pair <int, int>> glouton_solution;
vector<int> ps;

pair<set<int>, set<int>>  get_relations_of_person(int index);
vector<vector<int>> read_matrix_and_get_values(string path);

template<typename S>
auto select_random(const S& s, size_t n);

int get_p_one();
bool remove_contaminated_relation_from_infected_persons(int index);

void get_infected_persons();
void apply_glouton();
void apply_local_search(string path, string option);
void browse_infected_persons_left_to_right();
void browse_infected_persons_right_to_left();
void remove_infected_relations_from_cotaminated_person(pair<set<int>, set<int>> relations_state, int iter);
void reset_solution(string path);
void display_matrix();
void display_solution(string option);
void display(string option);



int main(int argc, char* argv[])
{
	srand(time(NULL));

	// string path = "./folder/exemplaires/40_400_15_0.txt";
	// string path = "./10_30_30_0.txt";
	//string path = "./folder/exemplaires/100_1000_20_0.txt";

	string e = argv[1];
	string path = argv[2];
	string k = argv[3];
	string rate_k = argv[4];
	K = std::stoi(rate_k);
	string option = "";

	if (argv[5] != NULL)
		option = argv[5];
	
	while (true)
	{
		if (option == "-p")
			apply_local_search(path, "-p");
		else
			apply_local_search(path, "");

		reset_solution(path);
		// cout << "-----------------------------------------------------------------" << endl;
	}

	return 0;

}

void apply_local_search(string path, string option)
{
	matrix = read_matrix_and_get_values(path);

	int diff = ((N / 2) - 1) - M;
	int perc = (10 * diff) / 100; // 25% des personnes contaminées
	if (perc < 1) perc = 1;

	int c = 0;
	while (c < diff)
	{
		apply_glouton();
		display_solution(option);

		int p1 = get_p_one();
		ps.push_back(p1);

		reset_solution(path);

		if (!ps.empty())
			for (int p : ps)
				infected_persons.insert(p);

		c++;
	}

	ps.clear();
}

void reset_solution(string path)
{
	persons_map.clear();
	glouton_solution.clear();
	infected_persons.clear();
	matrix = read_matrix_and_get_values(path);
}

void apply_glouton()
{
	get_infected_persons();
	browse_infected_persons_left_to_right();
	browse_infected_persons_right_to_left();

	if (has_value == false)
	{
		size_sol = glouton_solution.size();
		has_value = true;
	}
}

// on cherche dans notre solution la personne qui a le plus des relations infectées et le moins des relations saines.
int get_p_one() 
{
	int i = 0;
	int ratio = 0;
	map<int, pair<string, pair<set<int>, set<int>>>>::iterator current_p_one;

	int perc = 0.2 * N;
	while (i < perc)
	{
		int r = rand() % glouton_solution.size();
		int p_one = glouton_solution[r].first; // this person was contaminated
		int counter = 0; // nombre of infected persons removed

		for (int i = 0; i < glouton_solution.size(); i++)
		{
			if (glouton_solution[i].first == p_one)
				counter++;
		}

		auto it = persons_map.find(p_one);
		int k_i = counter + K; // nb des relations contaminées de p_one
		int h_i = it->second.second.first.size(); // nb des relations saines de p_one

		int ratio_i = 0;
		if (h_i != 0)
			ratio_i = k_i / h_i;

		if (ratio_i > ratio) // on cherche le rapport maximal
		{
			ratio = ratio_i;
			current_p_one = it;
		}

		i++;
	}

	return current_p_one->first;
}


void get_infected_persons()
{
	for (int inf_pers : infected_persons)
	{
		pair<set<int>, set<int>> relations_state = get_relations_of_person(inf_pers); // healthy or infected relation
		persons_map[inf_pers] = make_pair("infected", relations_state);
	}
}

pair<set<int>, set<int>> get_relations_of_person(int index)
{
	pair<set<int>, set<int>> relations_state;
	for (int j = 0; j < N; j++)
	{
		if (matrix[index][j] == 1)
		{
			if (infected_persons.find(j) != infected_persons.end())
				relations_state.second.insert(j); // j is found --> infected relation
			else
				relations_state.first.insert(j);  // j is not found --> healthy relation
		}
	}

	return relations_state;
}

void browse_infected_persons_left_to_right()
{
	for (auto it = persons_map.begin(); it != persons_map.end(); ++it)
	{
		for (auto iter = it->second.second.first.begin(); iter != it->second.second.first.end(); ++iter)
		{
			if (*iter > it->first) // take only the relations that are greater than the infected vertex
			{
				pair<set<int>, set<int>> relations_state = get_relations_of_person(*iter);
				if (relations_state.second.size() >= K) // if the number of infected persons is greater than K (propagation rate)
				{
					if (infected_persons.size() < ((N / 2) - 1))
					{
						infected_persons.insert(*iter);
						persons_map[*iter] = make_pair("contaminated", relations_state);
						if (remove_contaminated_relation_from_infected_persons(*iter++))
							if (iter != it->second.second.first.begin())
								iter--;
					}
					else
						remove_infected_relations_from_cotaminated_person(relations_state, *iter);
				}
			}
		}
	}
}

void browse_infected_persons_right_to_left()
{
	for (auto it = persons_map.rbegin(); it != persons_map.rend(); it++)
	{
		for (auto iter = it->second.second.first.begin(); iter != it->second.second.first.end(); ++iter)
		{
			if (*iter < it->first) // take only the relations that are smaller than the infected vertex
			{
				pair<set<int>, set<int>> relations_state = get_relations_of_person(*iter);
				if (relations_state.second.size() >= K) // if the number of infected persons is greater than K (propagation rate)
				{
					if (infected_persons.size() < ((N / 2) - 1))
					{
						infected_persons.insert(*iter);
						persons_map[*iter] = make_pair("contaminated", relations_state);
						if (remove_contaminated_relation_from_infected_persons(*iter++))
							if (iter != it->second.second.first.begin())
								iter--;
					}
					else
						remove_infected_relations_from_cotaminated_person(relations_state, *iter);
				}
			}
		}
	}
}

bool remove_contaminated_relation_from_infected_persons(int index)
{
	bool is_removed = false;

	for (auto it = persons_map.begin(); it != persons_map.end(); ++it)
	{
		auto iter = it->second.second.first.find(index);
		if (iter != it->second.second.first.end())
		{
			it->second.second.first.erase(index);
			it->second.second.second.insert(index);
			is_removed = true;
		}
	}

	return is_removed;
}

template<typename S>
auto select_random(const S& s, size_t n) {
	auto it = std::begin(s);
	// 'advance' the iterator n times
	std::advance(it, n);
	return it;
}
void remove_infected_relations_from_cotaminated_person(pair<set<int>, set<int>> relations_state, int iter)
{
	while (relations_state.second.size() >= K)
	{

		//auto r = rand() % relations_state.second.size(); // not _really_ random
		//auto n = *select_random(relations_state.second, r);
		//auto iter_prime = relations_state.second.find(n);



		auto iter_prime = relations_state.second.begin();
		pair<int, int> p(iter, *iter_prime);
		glouton_solution.push_back(p);
		matrix[iter][*iter_prime] = 0;
		matrix[*iter_prime][iter] = 0;
		relations_state.second.erase(*iter_prime);
	}
	persons_map[iter] = make_pair("healthy", relations_state);

}



void display_solution(string option)
{
	if (is_displayed == false)
	{
		display(option);
		is_displayed = true;
	}

	if (glouton_solution.size() < size_sol && is_displayed == true)
	{
		size_sol = glouton_solution.size();
		display(option);
	}
}

void display(string option)
{
	if (option == "")
		cout << size_sol << endl;
	else
	{
		for (auto const& s : glouton_solution)
			cout << s.first << " " << s.second << endl;
		cout << endl;
	}
}

vector<vector<int>> read_matrix_and_get_values(string path)
{
	vector<vector<int>> matrix;
	ifstream my_file(path);
	if (my_file.is_open())
	{
		string line;
		int i = 0;
		int j = 0;
		while (getline(my_file, line))
		{
			istringstream iss(line);
			vector<int> col;
			int val;
			while (iss >> val)
			{
				if (i == 0 && j == 0)
					N = val;
				else if (i == 0 && j == 1)
					M = val;
				else if (i > 0 && i <= N)
					col.push_back(val);
				else if (i > N)
					infected_persons.insert(val);
				j++;
			}
			if (!col.empty())
				matrix.push_back(col);
			i++;
		}
		my_file.close();
	}
	else cout << "Unable to open file";

	return matrix;
}

void display_matrix()
{
	for (int i = 0; i < matrix.size(); i++)
	{
		for (int j = 0; j < matrix[i].size(); j++)
			cout << matrix[i][j] << " ";
		cout << endl;
	}
	cout << endl;
}

