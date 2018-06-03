import pygal
import requests
from pygal.style import LightColorizedStyle as LCS, LightenStyle as LS

# Make an API call, and store the response.
url = 'https://api.github.com/search/repositories?q=language:python&sort=stars'
r = requests.get(url)
print("Status code:", r.status_code)

# Store API response in a variable.
response_dict = r.json()
print("Total repositories:", response_dict['total_count'])

# Explore information about the repositories.
repo_dicts = response_dict['items']
print("Repositories returned:", len(repo_dicts))

# repo_dict_0 = repo_dicts[0]
# print("\nKeys:", len(repo_dict_0))
# print(repo_dict_0)
# for k, v in sorted(repo_dict_0):
#     print(k)

names, plot_dicts = [], []
for repo_dict in repo_dicts:
    names.append(repo_dict['name'])
    if repo_dict['description']:
        desc = str(repo_dict['description'])
    else:
        desc = 'No description provided.'

    plot_dict = {
        'value': repo_dict['stargazers_count'],
        'label': desc,
        # Error: 'description' 的类型是NoneType , 它没有 decode 方法。
        # 所以要将 repo_dict['description'] 转为str
        'xlink': repo_dict['html_url'],
    }
    plot_dicts.append(plot_dict)

# Make visualization.
my_style = LS('#333366', base_style=LCS)

my_config = pygal.Config()
my_config.force_uri_protocol = 'http'
my_config.x_label_rotation = 45
my_config.show_legend = False
my_config.title_font_size = 24
my_config.label_font_size = 14
my_config.major_label_font_size = 18
my_config.truncate_label = 15
my_config.show_y_guides = False
my_config.width = 1000

chart = pygal.Bar(my_config, style=my_style)
chart.title = 'Most-Starred Python Projects on GitHub'
chart.x_labels = names

chart.add('', plot_dicts)
chart.render_to_file('output/python_repos.svg')
