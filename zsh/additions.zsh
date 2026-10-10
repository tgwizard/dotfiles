alias gti=git

# Prompt: full path and git branch on one line, `$` on the next.
# Colors match the robbyrussell theme; `$` turns red when the last command failed.
git_branch() {
  local branch=$(git branch 2>/dev/null | grep '^*' | sed -E 's/^\* //')
  if [[ -n "$branch" ]]; then
    echo " %{$fg_bold[red]%}$branch%{$reset_color%}"
  fi
}

PROMPT='%{$fg_bold[cyan]%}%~%{$reset_color%}$(git_branch)
%(?:%{$fg_bold[green]%}:%{$fg_bold[red]%})\$%{$reset_color%} '
