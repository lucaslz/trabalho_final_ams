#coding: utf-8

import json, gzip, os


def main():
    files_path = ''    
    candidates = ['bolsonaro'] #candidatos
    file_name = 'all_posts' #nome do arquivo com todas as postagens
    
    for candidate in candidates:
        #cria um arquivo para salvar alguns detalhes das postagens do comentário
        output_file = open('posts_details_comments_%s.tsv' % (candidate), 'w')
        #cabeçalho do arquivo
        output_file.write('post_id\tdate\tmessage\tnum_likes\tnum_angry\tnum_shares\n')
        print('********************************************************************************************************')
        print('\t\t\tREADING POSTS FROM %s ' % candidate)
        # caminho para o arquivo de post do candidato
        posts_file_path = '%s%s/%s.json.gz' % (files_path, candidate, file_name)
        # caminho dos comentários
        comments_path = '%s%s/comments/' % (files_path, candidate)
        print('\t\t\t%s' % posts_file_path)
        print('\t\t\t%s' % comments_path)   
        print('********************************************************************************************************')        
		
        #carregando o arquivo compactado
        with gzip.open(posts_file_path) as posts_file:
            for line in posts_file: 
                json_line = json.loads(line.strip())
                print (json_line)
                post_id = json_line['id']
                date = json_line['created_time']
                # a linha abaixo verifica se o campo message existe no dicionário
                msg = json_line['message'] if ('message' in json_line) else ''
                num_likes = json_line['reactions_like']['summary']['total_count']
                num_shares = json_line['shares']['count']
                num_angry = json_line['reactions_angry']['summary']['total_count']
                output_file.write('%s\t%s\t%s\t%d\t%d\t%d\n' % (post_id,date,json.dumps(msg),num_likes,num_angry,num_shares))


                
        
if __name__ == "__main__":
    main()

